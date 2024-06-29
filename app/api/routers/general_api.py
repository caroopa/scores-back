from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from database import get_db
from app.schemas.schemas import Score as ScoreSch
from app.api.routers.socket_api import manager
import app.services.general_service as service

router = APIRouter(prefix="/general", tags=["general"])


@router.get("", summary="Get all general data.")
def get_data(db: Session = Depends(get_db)):
    return service.get_data(db)


@router.put(
    "/calculate_total/{competitor_id}",
    summary="Calculate total score of current competitor.",
)
async def calculate_total(
    competitor_id: int, new_score: ScoreSch, db: Session = Depends(get_db)
):
    result = service.calculate_total(db, competitor_id, new_score)
    await manager.send_message(f"Total score updated for competitor {competitor_id}")
    return result


@router.post("/upload", summary="Upload file to create data.")
def create_data(file: UploadFile = File(...), db: Session = Depends(get_db)):
    return service.create_data(db, file)
