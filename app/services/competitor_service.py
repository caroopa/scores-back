from sqlalchemy.orm import Session
from sqlalchemy import func, desc, cast, Integer
from fastapi import HTTPException
import app.models.models as models
import app.schemas.schemas as schemas

Competitor = models.Competitor
School = models.School
Score = models.Score


def get_competitors_scores(db: Session, is_dan: bool):
    competitors = (
        db.query(
            Competitor.name,
            Competitor.category,
            School.acronym,
            func.sum(Score.total).label("total"),
        )
        .join(Score, Competitor.id_competitor == Score.competitor_id)
        .join(School, Score.school_id == School.id_school)
        .group_by(Competitor.id_competitor)
        .filter(cast(Competitor.category["is_dan"], Integer) == cast(is_dan, Integer))
        .order_by(desc("total"), desc(Competitor.category["value"]))
        .all()
    )

    if not competitors:
        raise HTTPException(status_code=404, detail="No se encontraron competidores.")

    competitors_scores = []

    for name, category, school, total in competitors:
        data = schemas.CompetitorScore(
            name=name,
            belt=category["belt"],
            school=schemas.School.get_school_name(school),
            total=total,
        )
        competitors_scores.append(data)

    return competitors_scores
