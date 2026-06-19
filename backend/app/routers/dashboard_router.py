from pathlib import Path

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.services import dashboard_service

router = APIRouter()

DASHBOARD_HTML = Path(__file__).resolve().parents[1] / "static" / "dashboard.html"


@router.get("", include_in_schema=False)
def dashboard_page():
    return FileResponse(DASHBOARD_HTML, media_type="text/html")


@router.get("/data")
def dashboard_data(db: Session = Depends(get_db)):
    return dashboard_service.get_dashboard(db)
