from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def root():
    import datetime
    hello = 3
    return {"message": "Hello World without errors"}
