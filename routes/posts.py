from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/posts", tags=["posts"])

# In-memory posts store for example
posts_db = []

class Post(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

@router.get("/get", response_model=List[Post])
def get_posts():
    return posts_db

@router.post("/add", response_model=Post)
def add_post(post: Post):
    posts_db.append(post)
    return post
