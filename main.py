from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db
from typing import Annotated

import app.models.models as models
import app.api.routers.general_api as general_api
import app.api.routers.instructor_api as instructor_api
import app.api.routers.competitor_api as competitor_api
import app.api.routers.socket_api as socket_api

app = FastAPI()

# CORS config
origins = ["https://scores-front.vercel.app", "http://scores-front.vercel.app"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include routers
db_dependency: Annotated[Session, Depends(get_db)] = Depends(get_db)
app.include_router(general_api.router, dependencies=[db_dependency])
app.include_router(instructor_api.router, dependencies=[db_dependency])
app.include_router(competitor_api.router, dependencies=[db_dependency])
app.include_router(socket_api.router, dependencies=[db_dependency])

# create tables
models.Base.metadata.create_all(bind=engine)
