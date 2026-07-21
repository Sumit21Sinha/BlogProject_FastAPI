from datetime import datetime
from pydantic import BaseModel, ConfigDict

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogUpdate(BaseModel):
    title: str
    content: str

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)