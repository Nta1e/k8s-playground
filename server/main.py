from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import os
from fastapi_sqlalchemy import DBSessionMiddleware
from dotenv import load_dotenv

from api import router

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

origins = [
	"http://localhost:5173",
]

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

