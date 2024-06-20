from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
import app.services.competitor_service as service

router = APIRouter()


@router.get("/competitors", summary="Get all competitors")
def get_competitors(db: Session = Depends(get_db)):
    return service.get_competitors(db)


@router.put(
    "/calculate_total/{competitor_id}",
    summary="Calculate total points of current competitor.",
)
def calculate_total(
    competitor_id: int,
    forms: int,
    jump: int,
    combat: int,
    db: Session = Depends(get_db),
):
    return service.calculate_total(db, competitor_id, forms, jump, combat)
