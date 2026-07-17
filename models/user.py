from sqlalchemy import Column, Integer, String, DateTime
from database.database import Base
import datetime
from sqlalchemy.orm import relationship

class user_table(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime)

blogs = relationship("Blog", back_populates="blog")