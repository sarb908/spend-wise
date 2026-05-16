from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str  # Raw password (input only)

class UserDisplay(BaseModel):
    access_token: str
    token_type: str
    class Config:
        from_attributes = True   # Pydantic v2
    