from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models import Role, User, Gender, UserUpdateRequest
app = FastAPI()
db: List[User] = [
    User( 
        id = uuid4(),
        first_name = "Edgar",
        last_name = "Santoscoy", 
        gender = Gender.male,
        roles = [Role.student]
    ),
    User(
        id = uuid4(),
        first_name = "Juan",
        last_name = "Martinez", 
        gender = Gender.male,
        roles = [Role.admin, Role.user]  
    )  
]
@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db;

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
                user.first_name = user_update.first_name
            if user_update.last_name is not None:
                user.last_name = user_update.last_name
            if user_update.middle_name is not None:
                user.middle_name = user_update.middle_name
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exist"
    )