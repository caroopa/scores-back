from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.schemas import TableData
from app.schemas.schemas import Score as ScoreSch
import app.models.models as models

Competitor = models.Competitor
Instructor = models.Instructor
School = models.School
Score = models.Score


def get_table_data(db: Session):
    competitors = (
        db.query(
            Competitor,
            Instructor.name,
            School.name,
            Score.forms,
            Score.combat,
            Score.jump,
            Score.total,
        )
        .join(Score, Competitor.id_competitor == Score.competitor_id)
        .join(Instructor, Score.instructor_id == Instructor.id_instructor)
        .join(School, Score.school_id == School.id_school)
        .all()
    )
    if not competitors:
        raise HTTPException(status_code=404, detail="No se encontraron datos.")

    table_data = []

    for (
        competitor,
        instructor_name,
        school_name,
        forms,
        combat,
        jump,
        total,
    ) in competitors:
        data = TableData(
            id_competitor=competitor.id_competitor,
            school=school_name,
            instructor=instructor_name,
            name=competitor.name,
            age=competitor.age,
            belt=competitor.belt,
            isDan=competitor.isDan,
            forms=forms,
            combat=combat,
            jump=jump,
            total=total,
        )
        table_data.append(data)

    return table_data


def calculate_total(db: Session, competitor_id: int, new_score: ScoreSch):
    # TODO: VALIDAR QUE JUMP SOLO SEA PARA DANES
    
    score = (
        db.query(Score).filter(Score.competitor_id == competitor_id).first()
    )
    if not score:
        raise HTTPException(status_code=404, detail="No se encontró el score.")

    score_forms = new_score.get_score(new_score.forms)
    score_combat = new_score.get_score(new_score.combat)
    score_jump = new_score.get_score(new_score.jump)

    score.forms = new_score.forms
    score.combat = new_score.combat
    score.jump = new_score.jump
    score.total = score_forms + score_combat + score_jump

    db.commit()
    db.refresh(score)
    return score.total
