from fastapi import APIRouter, Depends, HTTPException
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

@router.get("/", response_model=list[BlogResponse])
def get_all_blogs(db: Session = Depends(get_db)):
    return BlogService.get_all_blogs(db)

@router.get("/{blog_id}", response_model=BlogResponse)
def get_blog_by_id(blog_id: int, db: Session = Depends(get_db)):
    try:
        return BlogService.get_blog_by_id(blog_id, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))