from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.schemas import Score as ScoreSch
import app.services.competitor_service as service

router = APIRouter(prefix="/competitors", tags=["competitors"])


@router.get("", summary="Get all competitors.")
def get_table_data(db: Session = Depends(get_db)):
    return service.get_table_data(db)


@router.put(
    "/calculate_total/{competitor_id}",
    summary="Calculate total score of current competitor.",
)
def calculate_total(
    competitor_id: int, new_score: ScoreSch, db: Session = Depends(get_db)
):
    return service.calculate_total(db, competitor_id, new_score)
