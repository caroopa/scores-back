from sqlalchemy.orm import Session
from app.models.models import Competitor
from fastapi import HTTPException


def get_competitors(db: Session):
    competitors = db.query(Competitor).all()
    if not competitors:
        raise HTTPException(status_code=404, detail="No se encontraron competidores.")
    return competitors


def calculate_total(
    db: Session, competitor_id: int, forms: int, jump: int, combat: int
):
    competitor = (
        db.query(Competitor).filter(Competitor.id_competitor == competitor_id).first()
    )
    if not competitor:
        raise HTTPException(status_code=404, detail="No se encontró el competidor.")

    points_forms = competitor.get_points(forms)
    points_jump = competitor.get_points(jump)
    points_combat = competitor.get_points(combat)

    competitor.forms = forms
    competitor.jump = jump
    competitor.combat = combat
    competitor.total = points_forms + points_jump + points_combat

    db.commit()
    db.refresh(competitor)
    return competitor.total
