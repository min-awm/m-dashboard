from pydantic import BaseModel, Field


class RegisterSchema(BaseModel):
    name: str = Field(..., min_length=8, max_length=50)
    username: str = Field(..., min_length=8, max_length=50)
    password: str = Field(..., min_length=8, max_length=50)

class LoginSchema(BaseModel):
    username: str = Field(..., min_length=8, max_length=50)
    password: str = Field(..., min_length=8, max_length=50)
