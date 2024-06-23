from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
import app.services.instructor_service as service

router = APIRouter(prefix="/instructors", tags=["instructors"])


@router.get("", summary="Get all instructors scores.")
def get_instructors_scores(db: Session = Depends(get_db)):
    return service.get_instructors_scores(db)