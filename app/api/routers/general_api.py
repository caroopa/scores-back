from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session
from sqlalchemy import inspect
from database import get_db
from app.schemas.schemas import Score as ScoreSch
import app.services.general_service as service

router = APIRouter(prefix="/general", tags=["general"])


@router.get("", summary="Get all general data.")
def get_data(db: Session = Depends(get_db)):
    return service.get_data(db)


@router.put(
    "/calculate_total/{competitor_id}",
    summary="Calculate total score of current competitor.",
)
def calculate_total(
    competitor_id: int, new_score: ScoreSch, db: Session = Depends(get_db)
):
    return service.calculate_total(db, competitor_id, new_score)


@router.post("/upload", summary="Upload file to create data.")
def create_data(file: UploadFile = File(...), db: Session = Depends(get_db)):
    return service.create_data(db, file)

@router.get("/info")
def get_info(db: Session = Depends(get_db)):
    engine = db.get_bind()
    inspector = inspect(engine)
    table_info = {}
    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        table_info[table_name] = columns
    return table_info