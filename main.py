from fastapi import FastAPI
from supabase_client import supabase
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Agreement(BaseModel):
    id: int
    name: str
    address: str
    lat: float
    lon: float
    start_date: str
    duration_years: int
    next_service: str
    status: str

@app.get("/agreements", response_model=List[Agreement])
def get_agreements():
    data = supabase.table("agreements").select("*").execute()
    return data.data
