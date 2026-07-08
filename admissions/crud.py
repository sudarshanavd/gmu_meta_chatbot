"""
CRUD operations for GMU Admissions dashboard.
"""
import json
from datetime import datetime
from admissions.database import get_conn, init_db
from admissions.decoder import decode_interest


def _now() -> str:
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")


def upsert_student(wa_id: str, sender_name: str, phone: str, interest_code: str):
    """
    Insert a new student or update on repeat visit.
    Also logs every visit to bot_admissions_visits for the timeline chart.
    """
    try:
        decoded = decode_interest(interest_code)
        now = _now()
        conn = get_conn()
        try:
            cur = conn.cursor()
            # Check existing
            cur.execute("""
                SELECT id, visit_count, interests_json,
                       last_interest_code, last_level, last_faculty,
                       last_school, last_branch, last_label
                FROM bot_admissions_students
                WHERE wa_id = ?
            """, (wa_id,))
            row = cur.fetchone()
            if row:
                visit_count = (row["visit_count"] or 0) + 1
                try:
                    interests = json.loads(row["interests_json"] or "[]")
                except Exception:
                    interests = []
                if interest_code and interest_code not in interests:
                    interests.append(interest_code)

                db_level = row["last_level"] or "Unknown"
                db_faculty = row["last_faculty"] or "Unknown"
                db_school = row["last_school"] or "Unknown"
                db_branch = row["last_branch"] or "Unknown"

                new_level = decoded["level"]
                new_faculty = decoded["faculty"]
                new_school = decoded["school"]
                new_branch = decoded["branch"]

                # If the student has already been assigned a branch, we do NOT change any columns
                # unless a new non-Unknown branch is explicitly chosen.
                if db_branch != "Unknown":
                    if new_branch != "Unknown":
                        # A new branch is being assigned, so we update everything
                        updated_level = new_level
                        updated_faculty = new_faculty
                        updated_school = new_school
                        updated_branch = new_branch
                        updated_label = decoded["label"]
                        updated_interest_code = interest_code
                    else:
                        # No new branch selected, so we preserve all existing column values
                        updated_level = db_level
                        updated_faculty = db_faculty
                        updated_school = db_school
                        updated_branch = db_branch
                        updated_label = row["last_label"] or "Unknown"
                        updated_interest_code = row["last_interest_code"] or ""
                else:
                    # If no branch has been assigned yet, we update normally as they progress.
                    # To prevent generic messages (which decode to "Unknown") from resetting our progress,
                    # we only update a field if the new decoded value is not "Unknown".
                    updated_level = db_level
                    updated_faculty = db_faculty
                    updated_school = db_school
                    updated_branch = db_branch

                    # 1. Level Update
                    if new_level != "Unknown":
                        if new_level != db_level:
                            updated_level = new_level
                            updated_faculty = "Unknown"
                            updated_school = "Unknown"
                            updated_branch = "Unknown"

                    # 2. Faculty Update
                    if new_faculty != "Unknown":
                        if new_faculty != updated_faculty:
                            updated_faculty = new_faculty
                            updated_school = "Unknown"
                            updated_branch = "Unknown"

                    # 3. School Update
                    if new_school != "Unknown":
                        if new_school != updated_school:
                            updated_school = new_school
                            updated_branch = "Unknown"

                    # 4. Branch Update
                    if new_branch != "Unknown":
                        if new_branch != updated_branch:
                            updated_branch = new_branch

                    # Re-generate label from updated values
                    parts = []
                    if updated_level != "Unknown":
                        parts.append(updated_level)
                    if updated_faculty != "Unknown":
                        parts.append(updated_faculty)
                    if updated_school != "Unknown":
                        parts.append(updated_school)
                    if updated_branch != "Unknown":
                        parts.append(updated_branch)

                    updated_label = " › ".join(parts) if parts else "Unknown"
                    updated_interest_code = interest_code if interest_code else (row["last_interest_code"] or "")

                cur.execute("""
                    UPDATE bot_admissions_students SET
                        sender_name=?, phone=?,
                        last_interest_code=?, last_level=?, last_faculty=?,
                        last_school=?, last_branch=?, last_label=?,
                        interests_json=?, visit_count=?, last_seen=?
                    WHERE wa_id=?
                """, (
                    sender_name, phone,
                    updated_interest_code, updated_level, updated_faculty,
                    updated_school, updated_branch, updated_label,
                    json.dumps(interests), visit_count, now,
                    wa_id
                ))
            else:
                interests = [interest_code] if interest_code else []
                cur.execute("""
                    INSERT INTO bot_admissions_students
                        (wa_id, sender_name, phone,
                         last_interest_code, last_level, last_faculty,
                         last_school, last_branch, last_label,
                         interests_json, visit_count, first_seen, last_seen)
                    VALUES (?,?,?,?,?,?,?,?,?,?,1,?,?)
                """, (
                    wa_id, sender_name, phone,
                    interest_code, decoded["level"], decoded["faculty"],
                    decoded["school"], decoded["branch"], decoded["label"],
                    json.dumps(interests), now, now
                ))

            # Always log the visit
            cur.execute("""
                INSERT INTO bot_admissions_visits
                    (wa_id, interest_code, level, faculty, school, branch, label, visited_at)
                VALUES (?,?,?,?,?,?,?,?)
            """, (
                wa_id, interest_code,
                decoded["level"], decoded["faculty"],
                decoded["school"], decoded["branch"], decoded["label"],
                now
            ))
            conn.commit()
        finally:
            conn.close()
    except Exception as e:
        # Never break the main webhook flow
        print(f"[Admissions] upsert_student error: {e}")


def get_all_students(search: str = "", level: str = "", faculty: str = "",
                     page: int = 1, page_size: int = 50):
    """Return paginated student records with optional filters."""
    conn = get_conn()
    try:
        cur = conn.cursor()
        filters = ["1=1"]
        params = []
        if search:
            filters.append("(sender_name LIKE ? OR phone LIKE ? OR wa_id LIKE ?)")
            params += [f"%{search}%", f"%{search}%", f"%{search}%"]
        if level:
            filters.append("last_level = ?")
            params.append(level)
        if faculty:
            filters.append("last_faculty LIKE ?")
            params.append(f"%{faculty}%")

        where = " AND ".join(filters)
        cur.execute(f"SELECT COUNT(*) as cnt FROM bot_admissions_students WHERE {where}", params)
        total = cur.fetchone()["cnt"]

        offset = (page - 1) * page_size
        cur.execute(
            f"SELECT * FROM bot_admissions_students WHERE {where} ORDER BY last_seen DESC LIMIT ? OFFSET ?",
            params + [page_size, offset]
        )
        rows = [dict(r) for r in cur.fetchall()]
        return {"total": total, "page": page, "page_size": page_size, "students": rows}
    finally:
        conn.close()


def get_all_students_csv():
    """Return all students as a list of dicts for CSV export."""
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM bot_admissions_students ORDER BY last_seen DESC")
        return [dict(r) for r in cur.fetchall()]
    finally:
        conn.close()


def get_stats():
    """Return aggregated stats for dashboard charts."""
    conn = get_conn()
    try:
        cur = conn.cursor()

        # Total students
        cur.execute("SELECT COUNT(*) as cnt FROM bot_admissions_students")
        total_students = cur.fetchone()["cnt"]

        # Today's unique visitors
        today = datetime.utcnow().strftime("%Y-%m-%d")
        cur.execute(
            "SELECT COUNT(DISTINCT wa_id) as cnt FROM bot_admissions_visits WHERE visited_at LIKE ?",
            (f"{today}%",)
        )
        today_visitors = cur.fetchone()["cnt"]

        # By level (UG vs PG)
        cur.execute("""
            SELECT last_level as level, COUNT(*) as count
            FROM bot_admissions_students
            WHERE last_level IS NOT NULL AND last_level != 'Unknown'
            GROUP BY last_level ORDER BY count DESC
        """)
        by_level = [dict(r) for r in cur.fetchall()]

        # By faculty
        cur.execute("""
            SELECT last_faculty as faculty, COUNT(*) as count
            FROM bot_admissions_students
            WHERE last_faculty IS NOT NULL AND last_faculty != 'Unknown'
            GROUP BY last_faculty ORDER BY count DESC LIMIT 10
        """)
        by_faculty = [dict(r) for r in cur.fetchall()]

        # By school
        cur.execute("""
            SELECT last_school as school, COUNT(*) as count
            FROM bot_admissions_students
            WHERE last_school IS NOT NULL AND last_school != 'Unknown'
            GROUP BY last_school ORDER BY count DESC LIMIT 10
        """)
        by_school = [dict(r) for r in cur.fetchall()]

        # Visits per day (last 14 days)
        cur.execute("""
            SELECT substr(visited_at, 1, 10) as day, COUNT(*) as count
            FROM bot_admissions_visits
            GROUP BY day ORDER BY day DESC LIMIT 14
        """)
        daily_visits = [dict(r) for r in cur.fetchall()]
        daily_visits.reverse()

        # Top interest
        cur.execute("""
            SELECT last_label as label, COUNT(*) as count
            FROM bot_admissions_students
            WHERE last_label IS NOT NULL AND last_label != 'Unknown'
            GROUP BY last_label ORDER BY count DESC LIMIT 1
        """)
        row = cur.fetchone()
        top_interest = dict(row) if row else {"label": "N/A", "count": 0}

        return {
            "total_students": total_students,
            "today_visitors": today_visitors,
            "top_interest": top_interest,
            "by_level": by_level,
            "by_faculty": by_faculty,
            "by_school": by_school,
            "daily_visits": daily_visits,
        }
    finally:
        conn.close()
