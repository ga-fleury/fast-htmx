from fastapi import FastAPI
from pydantic import BaseModel

class NumberToMultiply(BaseModel):
    number: int
