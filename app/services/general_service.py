from sqlalchemy.orm import Session
from fastapi import HTTPException
import app.schemas.schemas as schemas
import app.models.models as models

Competitor = models.Competitor
Instructor = models.Instructor
School = models.School
Score = models.Score


def get_data(db: Session):
    competitors = (
        db.query(
            Competitor,
            Instructor.name,
            School.acronym,
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
        instructor,
        school,
        forms,
        combat,
        jump,
        total,
    ) in competitors:
        data = schemas.General(
            id_competitor=competitor.id_competitor,
            school=schemas.School.get_school_name(school),
            instructor=instructor,
            name=competitor.name,
            age=competitor.age,
            belt=competitor.category["belt"],
            is_dan=competitor.category["is_dan"],
            forms=forms,
            combat=combat,
            jump=jump,
            total=total,
        )
        table_data.append(data)

    return table_data


def calculate_total(db: Session, competitor_id: int, new_score: schemas.Score):
    # TODO: VALIDAR QUE JUMP SOLO SEA PARA DANES

    score = db.query(Score).filter(Score.competitor_id == competitor_id).first()
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
