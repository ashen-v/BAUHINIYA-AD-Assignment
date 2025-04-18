from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import CartItem, Product
from ..schema import Cart
from ..oauth2 import get_current_user

router = APIRouter(prefix="/cart", tags=["cart"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Cart)
def add_cart(cart: Cart, db : Session = Depends(get_db), user = Depends(get_current_user)):

    cart.user_id = user.id
    new_cart = CartItem(**cart.model_dump())
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart

@router.get("/", status_code=200)
def get_cart_items(db: Session = Depends(get_db), user = Depends(get_current_user)):
    cart_items = (
        db.query(CartItem)
        .filter(CartItem.user_id == user.id)
        .all()
    )

    result = []
    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if product:
            result.append({
                "id": item.id,
                "product_id": item.product_id,
                "quantity": item.quantity,
                "product": {
                    "name": product.name,
                    "price": product.price
                }
            })

    return result

@router.post("/checkout")
def checkout(db: Session = Depends(get_db), user = Depends(get_current_user)):
    cart_items = db.query(CartItem).filter(CartItem.user_id == user.id).all()

    if not cart_items:
        raise HTTPException(status_code=400, detail="Cart is empty")

    total = 0
    for item in cart_items:
        product = db.query(Product).filter(Product.id == item.product_id).first()
        if not product:
            continue
        total += product.price * item.quantity

    db.query(CartItem).filter(CartItem.user_id == user.id).delete()
    db.commit()

    return {"message": "Checkout successful", "total_price": total}


