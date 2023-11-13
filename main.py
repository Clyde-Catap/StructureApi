from fastapi import FastAPI
from Models.Beam.beammodel import BeamDataResponse
import random
import logging



app = FastAPI()

@app.get("/")
async def root():
    return {"www": 'working', 'this is data': 0}

@app.get("/beam/")
async def beam(Beam: BeamDataResponse):
    return