"""
JWT authentication for GMU Admissions dashboard.
Admin credentials stored in admissions/admin_creds.json (hashed with bcrypt).
"""
import os
import json
import hashlib
import hmac
import time
import base64
from pathlib import Path

ADMIN_CREDS_FILE = Path("admissions/admin_creds.json")
JWT_SECRET = os.getenv("ADMISSIONS_JWT_SECRET", "gmu-admissions-super-secret-2026")
JWT_ALGORITHM = "HS256"
JWT_EXPIRY_HOURS = int(os.getenv("ADMISSIONS_JWT_EXPIRY_HOURS", "24"))


# ── Simple password hashing (no external deps) ──────────────────────────────
def _hash_password(password: str) -> str:
    """Hash password using PBKDF2-HMAC-SHA256."""
    salt = os.urandom(16)
    key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 310_000)
    return base64.b64encode(salt + key).decode()


def _verify_password(password: str, stored_hash: str) -> bool:
    try:
        raw = base64.b64decode(stored_hash.encode())
        salt = raw[:16]
        stored_key = raw[16:]
        key = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 310_000)
        return hmac.compare_digest(key, stored_key)
    except Exception:
        return False


# ── Credential file management ──────────────────────────────────────────────
DEFAULT_PASSWORD = "admin123"
DEFAULT_USERNAME = "admin"


def _ensure_creds():
    """Create default credentials file if it doesn't exist."""
    if not ADMIN_CREDS_FILE.exists():
        ADMIN_CREDS_FILE.parent.mkdir(parents=True, exist_ok=True)
        creds = {
            "username": DEFAULT_USERNAME,
            "password_hash": _hash_password(DEFAULT_PASSWORD),
        }
        ADMIN_CREDS_FILE.write_text(json.dumps(creds, indent=2))
        print(f"[Admissions Auth] ✅ Default admin created — username: {DEFAULT_USERNAME}, password: {DEFAULT_PASSWORD}")
        print("[Admissions Auth] ⚠️  Please change the password via the dashboard Settings page.")
    return json.loads(ADMIN_CREDS_FILE.read_text())


def authenticate(username: str, password: str) -> bool:
    creds = _ensure_creds()
    if username != creds.get("username"):
        return False
    return _verify_password(password, creds["password_hash"])


def change_password(username: str, old_password: str, new_password: str) -> tuple[bool, str]:
    if not authenticate(username, old_password):
        return False, "Current password is incorrect."
    if len(new_password) < 6:
        return False, "New password must be at least 6 characters."
    creds = _ensure_creds()
    creds["password_hash"] = _hash_password(new_password)
    ADMIN_CREDS_FILE.write_text(json.dumps(creds, indent=2))
    return True, "Password changed successfully."


# ── Minimal JWT (no external deps: jose/PyJWT optional) ────────────────────
import struct


def _b64url_encode(data: bytes) -> str:
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def _b64url_decode(s: str) -> bytes:
    pad = 4 - len(s) % 4
    return base64.urlsafe_b64decode(s + "=" * (pad % 4))


def create_token(username: str) -> str:
    header = _b64url_encode(json.dumps({"alg": "HS256", "typ": "JWT"}).encode())
    payload = _b64url_encode(json.dumps({
        "sub": username,
        "iat": int(time.time()),
        "exp": int(time.time()) + JWT_EXPIRY_HOURS * 3600,
    }).encode())
    sig_input = f"{header}.{payload}".encode()
    sig = hmac.new(JWT_SECRET.encode(), sig_input, hashlib.sha256).digest()
    return f"{header}.{payload}.{_b64url_encode(sig)}"


def verify_token(token: str) -> dict | None:
    try:
        parts = token.split(".")
        if len(parts) != 3:
            return None
        header, payload_b64, sig_b64 = parts
        sig_input = f"{header}.{payload_b64}".encode()
        expected_sig = hmac.new(JWT_SECRET.encode(), sig_input, hashlib.sha256).digest()
        actual_sig = _b64url_decode(sig_b64)
        if not hmac.compare_digest(expected_sig, actual_sig):
            return None
        payload = json.loads(_b64url_decode(payload_b64))
        if payload.get("exp", 0) < time.time():
            return None
        return payload
    except Exception:
        return None
