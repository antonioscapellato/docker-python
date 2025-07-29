from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/users", tags=["users"])

# In-memory user store for example
users_db = []

class User(BaseModel):
    id: int
    name: str
    email: str

@router.get("/get", response_model=List[User])
def get_users():
    return users_db

@router.post("/add", response_model=User)
def add_user(user: User):
    users_db.append(user)
    return user
