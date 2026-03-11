from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from src.api.auth.dependencies import get_current_user

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Water Polo Stats API!"}