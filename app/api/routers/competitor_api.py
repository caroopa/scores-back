from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
import app.services.competitor_service as service

router = APIRouter(
    prefix='/competitor',
    tags=['competitor']
)

@router.get("", summary="Get all competitors")
def get_table_data(db: Session = Depends(get_db)):
    return service.get_table_data(db)


@router.put(
    "/calculate_total/{competitor_id}",
    summary="Calculate total points of current competitor.",
)
def calculate_total(
    competitor_id: int,
    forms: int,
    combat: int,
    jump: int,
    db: Session = Depends(get_db),
):
    return service.calculate_total(db, competitor_id, forms, combat, jump)
