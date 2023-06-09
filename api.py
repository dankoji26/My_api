from fastapi import FastAPI
from router import router

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Bienvenu(e) sur notre API."}

app.include_router(router)