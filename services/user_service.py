from sqlalchemy.orm import Session
from schemas.user import UserCreate
from  models.user import User
from auth.hashing import Hash
from auth.jwt_handler import create_access_token
from sqlalchemy.orm import Session
from models.blog import Blog
from models.user import User
from schemas.blog import BlogCreate
from fastapi.security import OAuth2PasswordRequestForm

class UserService:

    @staticmethod
    def register(user : UserCreate, db : Session):
        existing_user = db.query(User).filter(User.username == user.username).first()
        if existing_user:
            raise ValueError("User already exists")
        existing_email = db.query(User).filter(User.email == user.email).first()
        if existing_email:
            raise ValueError("Email already exists")
        hashed_password = Hash.hash_password(user.password)
        new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    @staticmethod
    def login(login_data : OAuth2PasswordRequestForm, db : Session):
        db_user = db.query(User).filter(User.email == login_data.username).first()
        if not db_user:
            raise ValueError("Invalid password or email")
        is_verified = Hash.verify_password(login_data.password, db_user.hashed_password)
        if not is_verified:
            raise ValueError("Invalid password or email")
        token = create_access_token({"sub": db_user.email})
        return token

