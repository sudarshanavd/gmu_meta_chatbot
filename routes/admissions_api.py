"""
FastAPI router for the GMU Admissions admin API.
All endpoints (except /login) require a Bearer JWT token.
"""
import io
import csv
from fastapi import APIRouter, HTTPException, Depends, Query, Request
from fastapi.responses import StreamingResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel

from admissions.auth import authenticate, create_token, verify_token, change_password
from admissions.crud import get_all_students, get_all_students_csv, get_stats
from admissions.database import init_db

router = APIRouter(prefix="/admissions", tags=["admissions"])
security = HTTPBearer(auto_error=False)

# ── Init DB on first import ──────────────────────────────────────────────────
init_db()


# ── Auth dependency ──────────────────────────────────────────────────────────
def require_auth(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    token: str = Query(None, description="Auth token via query parameter")
):
    token_str = None
    if credentials:
        token_str = credentials.credentials
    elif token:
        token_str = token

    if not token_str:
        raise HTTPException(status_code=401, detail="Not authenticated")

    payload = verify_token(token_str)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token.")
    return payload


# ── Request models ───────────────────────────────────────────────────────────
class LoginRequest(BaseModel):
    username: str
    password: str


class ChangePasswordRequest(BaseModel):
    username: str
    old_password: str
    new_password: str


# ── Endpoints ────────────────────────────────────────────────────────────────
@router.post("/login")
def login(req: LoginRequest):
    """Authenticate admin and return JWT token."""
    if not authenticate(req.username, req.password):
        raise HTTPException(status_code=401, detail="Invalid username or password.")
    token = create_token(req.username)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/change-password")
def change_pwd(req: ChangePasswordRequest, _=Depends(require_auth)):
    """Change the admin password."""
    ok, msg = change_password(req.username, req.old_password, req.new_password)
    if not ok:
        raise HTTPException(status_code=400, detail=msg)
    return {"message": msg}


@router.get("/students")
def students(
    search: str = Query("", description="Search by name/phone"),
    level: str = Query("", description="Filter by level: UG or PG"),
    faculty: str = Query("", description="Filter by faculty keyword"),
    page: int = Query(1, ge=1),
    page_size: int = Query(50, ge=1, le=200),
    _=Depends(require_auth),
):
    """Return paginated list of students."""
    return get_all_students(search=search, level=level, faculty=faculty,
                            page=page, page_size=page_size)


@router.get("/stats")
def stats(_=Depends(require_auth)):
    """Return aggregated stats for charts."""
    return get_stats()


@router.get("/export/csv")
def export_csv(request: Request, _=Depends(require_auth)):
    """Download all students as a CSV file without keywords/codes."""
    rows = get_all_students_csv()
    if not rows:
        raise HTTPException(status_code=404, detail="No student data available.")

    output = io.StringIO()
    # Clean standard fields only
    fields = [
        ("sender_name", "Name"),
        ("phone", "Phone"),
        ("wa_id", "WhatsApp ID"),
        ("last_level", "Level"),
        ("last_faculty", "Faculty"),
        ("last_school", "School"),
        ("last_branch", "Branch / Program"),
        ("visit_count", "Visit Count"),
        ("first_seen", "First Seen"),
        ("last_seen", "Last Seen"),
    ]
    
    # Write UTF-8 BOM for Excel compatibility
    output.write("\ufeff")
    
    writer = csv.writer(output)
    writer.writerow([label for _, label in fields])
    
    for row in rows:
        writer.writerow([row.get(key) or "" for key, _ in fields])
        
    output.seek(0)

    return StreamingResponse(
        io.BytesIO(output.getvalue().encode("utf-8")),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=gmu_admissions_students.csv"},
    )

