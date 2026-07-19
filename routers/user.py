from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db_dependency import get_db
from schemas.user import UserCreate, UserResponse
from services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/register", response_model=UserResponse, status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return UserService.register(user, db)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))