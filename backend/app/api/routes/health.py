from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.db.database import get_db

router = APIRouter(
    prefix="/api/health",
    tags=["Health"],
)


@router.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "World Tourism API is running",
    }


@router.get("/database")
def database_health_check(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT 1"))
    result.scalar()

    return {
        "status": "ok",
        "database": "connected",
    }
