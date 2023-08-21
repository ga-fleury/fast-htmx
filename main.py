from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

from models import NumberToMultiply

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("pages/index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("pages/about.html", {"request": request})

@app.get("/message")
async def message():
    return {"message": "nice message"}

@app.post("/multiply")
async def multiply_number(data: NumberToMultiply):
    print("multiply endpoint reached...")
    return data.number * 2

@app.get('/components/header')
async def get_header(request: Request):
    return templates.TemplateResponse("/components/header.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")