from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.table_data_sch import TableData
import app.models.models as models

Competitor = models.Competitor
Instructor = models.Instructor
School = models.School
Points = models.Points


def get_table_data(db: Session):
    competitors = (
        db.query(
            Competitor,
            Instructor.name,
            School.name,
            Points.forms,
            Points.combat,
            Points.jump,
            Points.total,
        )
        .join(Points, Competitor.id_competitor == Points.competitor_id)
        .join(Instructor, Points.instructor_id == Instructor.id_instructor)
        .join(School, Points.school_id == School.id_school)
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


def calculate_total(
    db: Session, competitor_id: int, forms: int, combat: int, jump: int
):
    competitor = (
        db.query(Competitor).filter(Competitor.id_competitor == competitor_id).first()
    )
    if not competitor:
        raise HTTPException(status_code=404, detail="No se encontró el competidor.")

    points_forms = Points.get_points(forms)
    points_combat = Points.get_points(combat)
    points_jump = Points.get_points(jump)

    competitor.forms = forms
    competitor.combat = combat
    competitor.jump = jump
    competitor.total = points_forms + points_combat + points_jump

    db.commit()
    db.refresh(competitor)
    return competitor.total
