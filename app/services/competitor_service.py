from sqlalchemy.orm import Session
from sqlalchemy import func, desc, cast, Integer
from fastapi import HTTPException
from app.schemas.schemas import CompetitorScore
import app.models.models as models

Competitor = models.Competitor
Score = models.Score


def get_competitors_scores(db: Session, is_dan: bool):
    competitors = (
        db.query(
            Competitor.name,
            Competitor.category,
            func.sum(Score.total).label("total"),
        )
        .join(Score)
        .group_by(Competitor.id_competitor)
        .filter(cast(Competitor.category["is_dan"], Integer) == cast(is_dan, Integer))
        .order_by(desc("total"), desc(Competitor.category["value"]))
        .all()
    )

    if not competitors:
        raise HTTPException(status_code=404, detail="No se encontraron competidores.")

    competitors_scores = []

    for name, category, total in competitors:
        print(category["is_dan"] == is_dan)
        data = CompetitorScore(name=name, belt=category["belt"], total=total)
        competitors_scores.append(data)

    return competitors_scores
