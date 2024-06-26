from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Instructor(Base):
    __tablename__ = "instructor"

    id_instructor = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    score = relationship("Score", back_populates="instructor")


class School(Base):
    __tablename__ = "school"

    id_school = Column(Integer, primary_key=True)
    acronym = Column(String, nullable=False)

    score = relationship("Score", back_populates="school")


class Competitor(Base):
    __tablename__ = "competitor"

    id_competitor = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    category = Column(JSON)

    score = relationship("Score", back_populates="competitor")


class Score(Base):
    __tablename__ = "score"

    competitor_id = Column(
        Integer, ForeignKey("competitor.id_competitor"), primary_key=True
    )
    instructor_id = Column(Integer, ForeignKey("instructor.id_instructor"))
    school_id = Column(Integer, ForeignKey("school.id_school"))

    forms = Column(Integer, default=0)
    combat = Column(Integer, default=0)
    jump = Column(Integer, default=0)
    total = Column(Integer, default=0)

    competitor = relationship("Competitor", back_populates="score")
    instructor = relationship("Instructor", back_populates="score")
    school = relationship("School", back_populates="score")
