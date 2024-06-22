from pydantic import BaseModel


class Points(BaseModel):
    forms: int = 0
    combat: int = 0
    jump: int = 0
    total: int = 0

    @staticmethod
    def get_points(key):
        places = {0: 0, 1: 9, 2: 5, 3: 2}
        return places.get(key, None)
