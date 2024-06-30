from app.schemas.schemas import Category

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
