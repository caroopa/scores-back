from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import app.services.competitor_service as service

router = APIRouter(prefix="/competitors", tags=["competitors"])


@router.get("/dan", summary="Get all competitors scores by Dan.")
def get_dan_scores(db: Session = Depends(get_db)):
    return service.get_competitors_scores(db, True)


@router.get("/color", summary="Get all competitors scores by Color.")
def get_color_scores(db: Session = Depends(get_db)):
    return service.get_competitors_scores(db, False)