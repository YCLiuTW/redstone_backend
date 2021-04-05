from pydantic import BaseModel

class User(BaseModel):
    username: str = None
    active: bool = False

class RequestData(BaseModel):
    image: str = None

class ResponseData(BaseModel):
    message: str = None
    status_code: int = 200

class ResponseToken(BaseModel):
    access_token: str = None
    token_type: str = 'bearer'
    status_code: int = 200