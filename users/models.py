from sqlalchemy import JSON, VARCHAR, Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False )
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)