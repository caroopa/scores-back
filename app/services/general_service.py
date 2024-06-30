from fastapi import HTTPException, UploadFile
from sqlalchemy.orm import Session
import pandas as pd
from io import StringIO
import app.schemas.schemas as schemas
import app.models.models as models
import app.utils.categories_data as categories_data

Competitor = models.Competitor
Instructor = models.Instructor
School = models.School
Score = models.Score


def get_data(db: Session):
    competitors = (
        db.query(Competitor, Instructor.name, School.acronym, Score)
        .join(Score, Competitor.id_competitor == Score.competitor_id)
        .join(Instructor, Score.instructor_id == Instructor.id_instructor)
        .join(School, Score.school_id == School.id_school)
        .order_by(Competitor.id_competitor)
        .all()
    )
    if not competitors:
        raise HTTPException(status_code=404, detail="No se encontraron datos.")

    table_data = []

    for competitor, instructor_name, school, score in competitors:
        data = schemas.General(
            id_competitor=competitor.id_competitor,
            school=schemas.School.get_school_name(school),
            instructor=instructor_name,
            name=competitor.name,
            age=competitor.age,
            belt=competitor.category["belt"],
            is_dan=competitor.category["is_dan"],
            forms=score.forms,
            combat=score.combat,
            jump=score.jump,
            total=score.total,
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


def create_data(db: Session, file: UploadFile):
    try:
        # Delete DB
        models.Base.metadata.drop_all(bind=db.get_bind())
        models.Base.metadata.create_all(bind=db.get_bind())

        # Read CSV
        # TODO: VALIDAR
        contents = file.file.read().decode("utf-8")
        df = pd.read_csv(StringIO(contents), sep=";")

        for _, row in df.iterrows():
            # Rows
            competitor_name = row["Apellido y Nombres"]
            competitor_age = row["Edad"]
            competitor_category = row["Graduación"]
            instructor_name = row["Instructor"]
            school_acronym = row["Esc."]

            # Instructor
            db_instructor = (
                db.query(Instructor).filter(Instructor.name == instructor_name).first()
            )
            if not db_instructor:
                db_instructor = Instructor()
                db_instructor.name = instructor_name
                db.add(db_instructor)
                db.commit()
                db.refresh(db_instructor)

            # School
            db_school = (
                db.query(School).filter(School.acronym == school_acronym).first()
            )
            if not db_school:
                db_school = School(acronym=school_acronym)
                db.add(db_school)
                db.commit()
                db.refresh(db_school)

            # Category
            category = schemas.Category.get_category_by_belt(
                competitor_category, categories_data.categories_data
            )
            if not category:
                raise HTTPException(
                    status_code=400,
                    detail=f"Categoría '{competitor_category}' no encontrada",
                )

            # Competitor
            db_competitor = Competitor(
                name=competitor_name,
                age=competitor_age,
                category=category.model_dump(),
            )
            db.add(db_competitor)
            db.commit()
            db.refresh(db_competitor)

            # Score
            db_score = Score(
                competitor_id=db_competitor.id_competitor,
                instructor_id=db_instructor.id_instructor,
                school_id=db_school.id_school,
                forms=0,
                combat=0,
                jump=0,
                total=0,
            )
            db.add(db_score)
            db.commit()
            db.refresh(db_score)

        return {"message": "Archivo cargado correctamente."}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error en la carga: {e}")
    finally:
        db.close()
