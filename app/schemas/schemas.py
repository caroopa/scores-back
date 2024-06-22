from pydantic import BaseModel


class TableData(BaseModel):
    id_competitor: int
    school: str
    instructor: str
    name: str
    age: int
    belt: str
    isDan: bool
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
