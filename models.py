from pydantic import BaseModel
from typing import Optional
from uuid import (
    
    UUID,
    uuid4
    
)
from enum import Enum
   
class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Roles(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
    
class User(BaseModel):
    id : Optional[UUID] = uuid4()
    first_name : str
    middle_name : Optional[str]
    last_name : str
    gender : Gender
    roles : list[Roles]
    
class UserMod(BaseModel):
    id : Optional[UUID] = uuid4()
    first_name : Optional[str]
    middle_name : Optional[str]
    last_name : Optional[str]