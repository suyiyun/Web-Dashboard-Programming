from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session

from . import crud, models
from .database import SessionLocal, engine

from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import plotly_express as px
import pandas as pd

models.Base.metadata.create_all(bind = engine)
app = FastAPI()
app.mount("/static", StaticFiles(directory = "static"), name = "static")

templates = Jinja2Templates(directory = "templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def welcome(request: Request, db: Session = Depends(get_db)):
    x = crud.get_salary(db)
    a = 5
    return templates.TemplateResponse("chart.html",{"request": request, "a": a})
