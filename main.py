from fastapi import FastAPI, Request, File, UploadFile
from fastapi import Body, Header, status, Response, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get("/greetings/{name}")
async def read_item(name: str) -> dict:
    return {"Message" : "Good day to you, " + name + "."}
