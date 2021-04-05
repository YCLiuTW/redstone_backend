from fastapi import FastAPI, Request, File, UploadFile
from fastapi import Body, Header, status, Response, HTTPException, Depends, Form
from pydantic import BaseModel
import base64, io, json
from PIL import Image
from data_model import ResponseData, RequestData, ResponseToken, User
from typing import Optional

app = FastAPI()

@app.get("/greetings/{name}")
async def read_item(name: str) -> dict:
    return {"Message" : "Good day to you, " + name + "."}

@app.post("/pass_image", response_model = ResponseData, status_code = 200)
async def test(item: RequestData, response: Response, authentication: Optional[str] = Header(None)) -> dict:
    response_data = ResponseData()
    try:
        image_bytes_str = item.image.encode('utf-8')
        image_b64str = base64.b64decode(image_bytes_str)
        image_data = io.BytesIO(image_b64str)
        image = Image.open(image_data)
        response_data.message = "ByPass complete."
        return response_data
    except:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        response_data.message = "Image integrity is not correct."
        response_data.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return response_data
