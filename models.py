from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

class EmailModel(BaseModel):
    email: EmailStr

class NumberToMultiply(BaseModel):
    number: int
