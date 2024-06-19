from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from database import get_db
from app.models.models import Competitor
import app.services.competitor_service as service

router = APIRouter()

@router.get(
    "/competitors",
    summary="Get all competitors",
    response_model=List[Competitor],
)
def get_competitors(db: Session = Depends(get_db)):
    return service.get_competitors(db)
