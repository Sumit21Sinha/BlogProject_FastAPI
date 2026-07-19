from sqlalchemy.orm import Session
from schemas.user import UserCreate
from  models.user import User
from auth.hashing import Hash

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