from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api_route
from app.env import Env

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=Env.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_route)
