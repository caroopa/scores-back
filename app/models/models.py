from sqlalchemy import Column, Integer, String, BigInteger, Boolean, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Instructor(Base):
    __tablename__ = "instructor"

    id_instructor = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    points = relationship("Points", back_populates="instructor")


class School(Base):
    __tablename__ = "school"

    id_school = Column(BigInteger, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    acronym = Column(String, nullable=False)

    points = relationship("Points", back_populates="school")


class Competitor(Base):
    __tablename__ = "competitor"

    id_competitor = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    belt = Column(String, nullable=False)
    isDan = Column(Boolean, nullable=False)

    points = relationship("Points", back_populates="competitor")


class Points(Base):
    __tablename__ = "points"

    id_points = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    competitor_id = Column(BigInteger, ForeignKey("competitor.id_competitor"))
    instructor_id = Column(BigInteger, ForeignKey("instructor.id_instructor"))
    school_id = Column(BigInteger, ForeignKey("school.id_school"))
    
    forms = Column(Integer, default=0)
    combat = Column(Integer, default=0)
    jump = Column(Integer, default=0)
    total = Column(Integer, default=0)

    competitor = relationship("Competitor", back_populates="points")
    instructor = relationship("Instructor", back_populates="points")
    school = relationship("School", back_populates="points")