from fastapi import FastAPI, Depends
from database import engine
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db
from fastapi.middleware.cors import CORSMiddleware

import app.models.models as models
import app.api.routers.competitor_api as competitor_api
import app.api.routers.instructor_api as instructor_api
import data

app = FastAPI()

# CORS config
origins = ["http://localhost", "http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
db_dependency: Annotated[Session, Depends(get_db)] = Depends(get_db)
app.include_router(competitor_api.router, dependencies=[db_dependency])
app.include_router(instructor_api.router, dependencies=[db_dependency])

# create tables
models.Base.metadata.create_all(bind=engine)

# insert data
def insert_data_by_a_dict(dict_of_data: dict):
    model = dict_of_data["model"]
    elements = dict_of_data["listOfElements"]
    attribute_name = dict_of_data["property"]

    for element in elements:
        attribute = getattr(model, attribute_name, None)
        attributeToCompare = getattr(element, attribute_name, None)
        element_exist = db.query(model).filter(attribute == attributeToCompare).first()
        if not element_exist:
            db.add(element)
            db.commit()


def insert_ternary(dict_data_ternary: dict):
    model = dict_data_ternary["model"]
    elements = dict_data_ternary["listOfElements"]

    first_attribute_name = dict_data_ternary["property"][0]
    second_attribute_name = dict_data_ternary["property"][1]

    for ternary_element in elements:

        first_attribute = getattr(model, first_attribute_name, None)
        first_attribute_to_compare = getattr(
            ternary_element, first_attribute_name, None
        )

        second_attribute = getattr(model, second_attribute_name, None)
        second_attribute_to_compare = getattr(
            ternary_element, second_attribute_name, None
        )

        element_exist = (
            db.query(model)
            .filter(
                first_attribute == first_attribute_to_compare,
                second_attribute == second_attribute_to_compare,
            )
            .first()
        )
        if not element_exist:
            db.add(ternary_element)
            db.commit()
            
db = next(get_db())
insert_data_by_a_dict(data.competitor_data)
insert_data_by_a_dict(data.instructors_data)
insert_data_by_a_dict(data.schools_data)
insert_ternary(data.score_data)
