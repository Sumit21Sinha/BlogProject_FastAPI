from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from auth.oauth2 import get_current_user
from database.db_dependency import get_db
from models.user import User
from schemas.blog import BlogCreate, BlogResponse
from services.blog_service import BlogService

router = APIRouter(prefix="/blogs", tags=["Blogs"])

@router.post("/", response_model=BlogResponse, status_code=201)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return BlogService.create_blog(blog, db, current_user)