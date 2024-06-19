from pydantic import BaseModel

# POR AHORA NO ESTÁ EN USO

class CompetitorBase(BaseModel):
	school: str
	instructor: str
	name: str
	age: int
	belt: str
	isDan: bool
	forms: int = 0
	jump: int = 0
	combat: int = 0
	total: int = 0

class CompetitorCreate(CompetitorBase):
	password: str

class Competitor(CompetitorBase):
	id_competitor: int

	class Config:
			orm_mode = True