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

class TokenData(BaseModel):
    id : Optional[str] = None

class ProductManage(BaseModel):
    name : str
    price : int
    quantity : int

class Cart(BaseModel):
    user_id : int
    product_id : int
    quantity : Optional[int] = 1


