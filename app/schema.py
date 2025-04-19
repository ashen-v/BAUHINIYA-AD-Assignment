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
    user_id : Optional [int] = None
    product_id : int
    quantity : Optional[int] = 1

class Total_data(BaseModel):
    total_stock : int
    total_products : int
    total_users : int


