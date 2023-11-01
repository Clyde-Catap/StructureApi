from fastapi import FastAPI
import random
import logging



app = FastAPI()

@app.get("/")
async def root():
    return {"www":'working', 'this is data': 0}