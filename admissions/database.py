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


class DBCursorWrapper:
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self, query, params=None):
        if DB_TYPE == "mysql" and query:
            # Replace placeholder ? with %s for MySQL compatibility
            query = query.replace("?", "%s")
        if params is not None:
            return self.cursor.execute(query, params)
        return self.cursor.execute(query)

    def __enter__(self):
        if hasattr(self.cursor, "__enter__"):
            self.cursor.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self.cursor, "__exit__"):
            return self.cursor.__exit__(exc_type, exc_val, exc_tb)

    def __getattr__(self, name):
        return getattr(self.cursor, name)


class DBConnectionWrapper:
    def __init__(self, conn):
        self.conn = conn

    def cursor(self, *args, **kwargs):
        cur = self.conn.cursor(*args, **kwargs)
        return DBCursorWrapper(cur)

    def __enter__(self):
        if hasattr(self.conn, "__enter__"):
            self.conn.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(self.conn, "__exit__"):
            return self.conn.__exit__(exc_type, exc_val, exc_tb)

    def __getattr__(self, name):
        return getattr(self.conn, name)


def get_conn():
    if DB_TYPE == "mysql":
        conn = _mysql_conn()
    else:
        conn = _sqlite_conn()
    return DBConnectionWrapper(conn)


# ── Schema init ──────────────────────────────────────────────────────────────
CREATE_STUDENTS_SQL = """
CREATE TABLE IF NOT EXISTS bot_admissions_students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    wa_id VARCHAR(255) NOT NULL UNIQUE,
    sender_name VARCHAR(255),
    phone VARCHAR(30),
    last_interest_code VARCHAR(100),
    last_level VARCHAR(100),
    last_faculty VARCHAR(255),
    last_school VARCHAR(255),
    last_branch VARCHAR(255),
    last_label VARCHAR(255),
    interests_json TEXT DEFAULT '[]',
    visit_count INT DEFAULT 1,
    first_seen DATETIME,
    last_seen DATETIME
);
"""

CREATE_VISITS_SQL = """
CREATE TABLE IF NOT EXISTS bot_admissions_visits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    wa_id VARCHAR(255) NOT NULL,
    interest_code VARCHAR(100),
    level VARCHAR(100),
    faculty VARCHAR(255),
    school VARCHAR(255),
    branch VARCHAR(255),
    label VARCHAR(255),
    visited_at DATETIME
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
