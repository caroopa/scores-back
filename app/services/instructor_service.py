from sqlalchemy.orm import Session
from sqlalchemy import func
from fastapi import HTTPException
from app.schemas.schemas import InstructorScore
import app.models.models as models

Instructor = models.Instructor
Score = models.Score


def get_instructors_scores(db: Session):
    instructors = (
        db.query(Instructor.name, func.sum(Score.total).label("total"))
        .join(Score, Score.instructor_id == Instructor.id_instructor)
        .group_by(Instructor.id_instructor)
        .all()
    )

    if not instructors:
        raise HTTPException(status_code=404, detail="No se encontraron instructores.")

    instructors_scores = []

    for name, total in instructors:
        data = InstructorScore(name=name, total=total)
        instructors_scores.append(data)

    return instructors_scores
