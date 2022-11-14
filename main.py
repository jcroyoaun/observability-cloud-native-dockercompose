from http.client import HTTPMessage
from typing import List
from uuid import uuid4
from fastapi import FastAPI, Depends, HTTPException
from models import *
from database import engine, SessionLocal
import models 
from sqlalchemy.orm import Session
from prometheus_client import start_http_server, Counter
import http.server

METRICS_PORT = 8001
REQUEST_COUNT = Counter('app_request_count', 'Total / http request count')
REQUEST_COUNT_USERS = Counter('app_request_count_users', 'Total /api/v1/users http request count')

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

start_http_server(METRICS_PORT)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def create_database():
    REQUEST_COUNT.inc()
    return {"Hello": "World!"}

@app.get("/api/v1/users")
async def fetch_users(db: Session = Depends(get_db)):
    REQUEST_COUNT_USERS.inc()
    return db.query(models.User).all()

@app.post("/api/v1/users")
async def register_user(user: UserModel, db: Session = Depends(get_db)):
    user_model = models.User()
    user_model.id = user.id
    user_model.first_name = user.first_name
    user_model.last_name = user.last_name
    user_model.middle_name = user.middle_name
    db.add(user_model)
    db.commit()
    return {"id": user.id }

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_model = db.query(models.User)
    for user in user_model:
        print(user_id)
        print(user.id)
        if user.id == user_id:
            db.delete(user)
            db.commit()
            return { f"user with id: {user_id} was deleted" }

    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )
  
# @app.put("/api/v1/users/{user_id}")