from typing import Optional, List
#from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from enum import Enum
from sqlalchemy import Boolean, Column, Integer, String
from database import Base
#from sqlalchemy.dialects.postgresql import UUID

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    mentor = "mentor"
    user = "user"
    student = "student"

class User (Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    middle_name = Column(String)
    #gender: Gender 
    #roles: List[Role]

class UserModel (BaseModel):
    id: int
    first_name: str
    last_name: str
    middle_name: Optional[str]
    # gender: Gender 
    # roles: List[Role]

    #gender: Gender 
    #roles: List[Role]
# class UserUpdateRequest(Base):
#     first_name: Optional[str]
#     last_name: Optional[str]
#     middle_name: Optional[str]
#     #roles: Optional[List[Role]]

