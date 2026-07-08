from contextlib import asynccontextmanager
import os
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi import Request

from routes import webhook
from routes.admissions_api import router as admissions_router

app = FastAPI(
    title="GMU WhatsApp API",
    description="API for GMU WhatsApp application",
    version="1.0.0",
)

# ── WhatsApp webhook ─────────────────────────────────────────────────────────
app.include_router(webhook.router)

# ── Admissions admin API ─────────────────────────────────────────────────────
app.include_router(admissions_router)

# ── React SPA static assets ──────────────────────────────────────────────────
DASHBOARD_DIST = Path("dashboard/dist")
if DASHBOARD_DIST.exists():
    # Serve the full dist/ dir at /dashboard-assets so the built paths
    # like /dashboard-assets/assets/index-xxx.js resolve correctly.
    app.mount(
        "/dashboard-assets",
        StaticFiles(directory=str(DASHBOARD_DIST)),
        name="dashboard-assets",
    )

    @app.get("/dashboard", include_in_schema=False)
    @app.get("/dashboard/{full_path:path}", include_in_schema=False)
    async def serve_dashboard(full_path: str = ""):
        index = DASHBOARD_DIST / "index.html"
        return FileResponse(str(index))

# Allows both `uvicorn main:app` and `uvicorn main:main`.
main = app
