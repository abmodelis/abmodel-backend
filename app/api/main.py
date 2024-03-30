from fastapi import FastAPI
from app.api.routes import api_route

app = FastAPI()
app.include_router(api_route)


@app.get("/")
async def root():
    return {"message": "Hello World"}
