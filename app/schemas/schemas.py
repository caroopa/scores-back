from pydantic import BaseModel
from app.models.models import Competitor


class General(BaseModel):
    id_competitor: int
    school: str
    instructor: str
    name: str
    age: int
    belt: str
    is_dan: bool
    forms: int = 0
    combat: int = 0
    jump: int = 0
    total: int = 0


class Score(BaseModel):
    forms: int = 0
    combat: int = 0
    jump: int = 0

    @staticmethod
    def get_score(key):
        places = {0: 0, 1: 9, 2: 5, 3: 2}
        return places.get(key, None)


class InstructorScore(BaseModel):
    name: str
    total: int


class CompetitorScore(BaseModel):
    name: str
    belt: str
    school: str
    total: int


class Category(BaseModel):
    belt: str
    is_dan: bool
    value: int


class School(BaseModel):
    acronym: str
    name: str

    @staticmethod
    def get_school_name(acronym):
        switcher = {
            "EK": "Escuela Koguryo",
            "CS": "Círculo Samguk",
            "TN": "Taekwondo Navarro",
            "ECK": "Escuela Círculo Kwon",
            "TRA": "Taekwondo República Argentina",
            "EKH": "Escuela Kyun Hyung",
            "ECT": "Escuela Cristiana Taekwondo",
            "EDG": "Escuela Damián García",
            "EKU": "Escuela Kumgang",
            "EWK": "Escuela Won Kang",
            "ESC": "Escuela Sabom",
            "ETU": "Escuela Taekwondo Unido",
            "DWA": "Dae Wan Gam",
        }
        return switcher.get(acronym, acronym)
