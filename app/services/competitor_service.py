from sqlalchemy.orm import Session
from app.models.models import Competitor
from fastapi import HTTPException

def get_competitors(db: Session):
  competitors = db.query(Competitor).all()
  if not competitors:
    raise HTTPException(status_code=404, detail="No se encontraron competidores.")
  return competitors