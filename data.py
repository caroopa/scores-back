import app.models.models as models

Competitor = models.Competitor
Instructor = models.Instructor
School = models.School
Score = models.Score

competitor_data = {
    "model": Competitor,
    "listOfElements": [
        Competitor(
            id_competitor=22,
            name="AGUIRRE LAUTARO GABRIEL",
            age=15,
            belt="AZUL",
            isDan=False,
        ),
        Competitor(
            id_competitor=23,
            name="ALBARENGA LISANDRO JORGE",
            age=13,
            belt="VERDE",
            isDan=False,
        ),
        Competitor(
            id_competitor=24,
            name="ALBARRACIN CELESTE MAIA",
            age=7,
            belt="BLANCO",
            isDan=False,
        ),
        Competitor(
            id_competitor=25,
            name="ALBARRACIN LORENZO",
            age=7,
            belt="BLANCO",
            isDan=False,
        ),
        Competitor(
            id_competitor=26,
            name="ALBARRACIN MATHEO AGUSTIN",
            age=11,
            belt="BLANCO PUNTA AMARILLA",
            isDan=False,
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
    "listOfElements": [School(id_school=1, name="EK", acronym="EK")],
    "property": "name",
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
