from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
import app.services.competitor_service as service

router = APIRouter()

@router.get("/competitors", summary="Get all competitors")
def get_competitors(db: Session = Depends(get_db)):
  return service.get_competitors(db)