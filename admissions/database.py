"""
SQLite database layer for GMU Admissions dashboard.
Easily switchable to MySQL by setting DB_TYPE=mysql in .env.
"""
import os
import sqlite3
import json
from datetime import datetime, date
from typing import Optional

# ── Config ──────────────────────────────────────────────────────────────────
DB_PATH = os.getenv("ADMISSIONS_DB_PATH", "admissions/admissions.db")
DB_TYPE = os.getenv("DB_TYPE", "sqlite").lower()   # "sqlite" or "mysql"

# MySQL config (only used when DB_TYPE=mysql)
MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
MYSQL_PORT = int(os.getenv("MYSQL_PORT", "3306"))
MYSQL_USER = os.getenv("MYSQL_USER", "root")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
MYSQL_DB = os.getenv("MYSQL_DATABASE", "gmu_admissions")


# ── Connection helpers ───────────────────────────────────────────────────────
def _sqlite_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


def _mysql_conn():
    import pymysql
    return pymysql.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB,
        cursorclass=pymysql.cursors.DictCursor,
    )


def get_conn():
    if DB_TYPE == "mysql":
        return _mysql_conn()
    return _sqlite_conn()


# ── Schema init ──────────────────────────────────────────────────────────────
CREATE_STUDENTS_SQL = """
CREATE TABLE IF NOT EXISTS bot_admissions_students (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    wa_id       TEXT    NOT NULL UNIQUE,
    sender_name TEXT,
    phone       TEXT,
    last_interest_code  TEXT,
    last_level          TEXT,
    last_faculty        TEXT,
    last_school         TEXT,
    last_branch         TEXT,
    last_label          TEXT,
    interests_json      TEXT DEFAULT '[]',
    visit_count         INTEGER DEFAULT 1,
    first_seen          TEXT,
    last_seen           TEXT
);
"""

CREATE_VISITS_SQL = """
CREATE TABLE IF NOT EXISTS bot_admissions_visits (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    wa_id       TEXT    NOT NULL,
    interest_code TEXT,
    level       TEXT,
    faculty     TEXT,
    school      TEXT,
    branch      TEXT,
    label       TEXT,
    visited_at  TEXT
);
"""


def init_db():
    """Create tables if they don't exist."""
    conn = get_conn()
    try:
        cur = conn.cursor()
        cur.execute(CREATE_STUDENTS_SQL)
        cur.execute(CREATE_VISITS_SQL)
        conn.commit()
    finally:
        conn.close()
