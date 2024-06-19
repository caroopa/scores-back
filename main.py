from fastapi import FastAPI, Depends
from database import engine
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db

import app.models.models as models
import app.api.routers.competitor_api as competitor_api
from data import competitor_data

app = FastAPI()

# include routers
db_dependency : Annotated[Session, Depends(get_db)] = Depends(get_db)
app.include_router(competitor_api.router, dependencies=[db_dependency])

# create tables
models.Base.metadata.create_all(bind=engine)

# insert data
def insert_data_by_a_dict(dict_of_data: dict, db: Session):
    model = dict_of_data['model']
    elements = dict_of_data['listOfElements']
    attribute_name = dict_of_data['property']

    for element in elements:
        attribute = getattr(model, attribute_name, None)
        attributeToCompare = getattr(element, attribute_name, None)
        element_exist = db.query(model).filter(attribute == attributeToCompare).first()
        if not element_exist:
            db.add(element)
            db.commit()
db = next(get_db())
insert_data_by_a_dict(competitor_data, db)