from sqlalchemy.orm import Session
from schemas.user import UserCreate
from  models.user import User
from auth.hashing import Hash
from auth.jwt_handler import create_access_token
from sqlalchemy.orm import Session
from models.blog import Blog
from models.user import User
from schemas.blog import BlogCreate

class BlogService:

    @staticmethod
    def create_blog(blog: BlogCreate, db: Session, current_user: User):
        new_blog = Blog(title=blog.title, content=blog.content, owner_id=current_user.id)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog

    @staticmethod
    def get_all_blogs(db: Session):
        blogs = db.query(Blog).all()
        return blogs

    @staticmethod
    def get_blog_by_id(blog_id: int, db: Session):
        blog = (db.query(Blog).filter(Blog.id == blog_id).first())
        if blog is None:
            raise ValueError("Blog not found")
        return blog