from fastapi import FastAPI
from database.database import Base, engine
from models.user import User
from models.blog import Blog
from routers.user import router as user_router

app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(user_router)

@app.get("/")
def root():
    return {"Message:" : "Blog API running"}