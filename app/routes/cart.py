from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import CartItem
from ..schema import Cart
from ..oauth2 import get_current_user

router = APIRouter(prefix="/cart", tags=["cart"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Cart)
def add_cart(cart: Cart, db : Session = Depends(get_db)):

    new_cart = CartItem(**cart.model_dump())
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart

