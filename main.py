from fastapi import FastAPI
from database.database import Base, engine
from models.user import User
from models.blog import Blog

app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get("/")
def root():
    return {"Message:" : "Blog API running"}