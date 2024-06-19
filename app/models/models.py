from sqlalchemy import Column, Integer, String, BigInteger, Boolean
from database import Base

class Competitor(Base):
    __tablename__ = "competitor"

    id_competitor = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    school = Column(String)
    instructor = Column(String)
    name = Column(String)
    age = Column(Integer)
    belt = Column(String)
    isDan = Column(Boolean)
    forms = Column(Integer, default=0)
    jump = Column(Integer, default=0)
    combat = Column(Integer, default=0)
    total = Column(Integer, default=0)