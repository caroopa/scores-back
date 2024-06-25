import app.models.models as models
import app.schemas.schemas as schemas

Competitor = models.Competitor
Instructor = models.Instructor
School = models.School
Score = models.Score
Category = schemas.Category

categories_data = {
    "white": Category(belt="BLANCO", is_dan=False, value=1),
    "white-y": Category(belt="BLANCO PUNTA AMARILLA", is_dan=False, value=2),
    "yellow": Category(belt="AMARILLO", is_dan=False, value=3),
    "yellow-g": Category(belt="AMARILLO PUNTA VERDE", is_dan=False, value=4),
    "green": Category(belt="VERDE", is_dan=False, value=5),
    "green-b": Category(belt="VERDE PUNTA AZUL", is_dan=False, value=6),
    "blue": Category(belt="AZUL", is_dan=False, value=7),
    "blue-r": Category(belt="AZUL PUNTA ROJA", is_dan=False, value=8),
    "red": Category(belt="ROJO", is_dan=False, value=9),
    "red-b": Category(belt="ROJO PUNTA NEGRA", is_dan=False, value=10),
    "danI": Category(belt="PRIMER DAN", is_dan=True, value=11),
    "danII": Category(belt="SEGUNDO DAN", is_dan=True, value=12),
    "danIII": Category(belt="TERCER DAN", is_dan=True, value=13),
    "danIV": Category(belt="CUARTO DAN", is_dan=True, value=14),
    "danV": Category(belt="QUINTO DAN", is_dan=True, value=15),
    "danVI": Category(belt="SEXTO DAN", is_dan=True, value=16),
    "danVII": Category(belt="SÉPTIMO DAN", is_dan=True, value=17),
    "danVIII": Category(belt="OCTAVO DAN", is_dan=True, value=18),
    "danIX": Category(belt="NOVENO DAN", is_dan=True, value=19),
}

competitor_data = {
    "model": Competitor,
    "listOfElements": [
        Competitor(
            id_competitor=22,
            name="AGUIRRE LAUTARO GABRIEL",
            age=15,
            category=categories_data["white"].model_dump(),
        ),
        Competitor(
            id_competitor=23,
            name="ALBARENGA LISANDRO JORGE",
            age=13,
            category=categories_data["white"].model_dump(),
        ),
        Competitor(
            id_competitor=24,
            name="ALBARRACIN CELESTE MAIA",
            age=7,
            category=categories_data["yellow"].model_dump(),
        ),
        Competitor(
            id_competitor=25,
            name="ALBARRACIN LORENZO",
            age=7,
            category=categories_data["yellow"].model_dump(),
        ),
        Competitor(
            id_competitor=26,
            name="ALBARRACIN MATHEO AGUSTIN",
            age=11,
            category=categories_data["danI"].model_dump(),
        ),
    ],
    "property": "name",
}

instructors_data = {
    "model": models.Instructor,
    "listOfElements": [
        Instructor(id_instructor=1, name="OBREGON HECTOR DAVID"),
        Instructor(id_instructor=2, name="GADEA BARBARA SOFÍA"),
        Instructor(id_instructor=3, name="LUIS GERMÁN MAXIMILIANO"),
        Instructor(id_instructor=4, name="TELLO SANTIAGO"),
    ],
    "property": "name",
}

schools_data = {
    "model": models.School,
    "listOfElements": [
        School(id_school=1, acronym="EK"),
    ],
    "property": "acronym",
}

score_data = {
    "model": models.Score,
    "listOfElements": [
        Score(
            competitor_id=22,
            instructor_id=1,
            school_id=1,
            forms=0,
            combat=0,
            jump=0,
            total=0,
        ),
        Score(
            competitor_id=23,
            instructor_id=2,
            school_id=1,
            forms=0,
            combat=0,
            jump=0,
            total=0,
        ),
        Score(
            competitor_id=24,
            instructor_id=3,
            school_id=1,
            forms=0,
            combat=0,
            jump=0,
            total=0,
        ),
        Score(
            competitor_id=25,
            instructor_id=4,
            school_id=1,
            forms=0,
            combat=0,
            jump=0,
            total=0,
        ),
        Score(
            competitor_id=26,
            instructor_id=4,
            school_id=1,
            forms=0,
            combat=0,
            jump=0,
            total=0,
        ),
    ],
    "property": ["competitor_id", "instructor_id"],
}
