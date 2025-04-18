from pydantic import BaseModel, EmailStr
from typing import Optional

class Register(BaseModel):
    username: str
    email:EmailStr
    address:str
    phone1:int
    phone2:int
    password:str
    role: Optional[str] = "user"