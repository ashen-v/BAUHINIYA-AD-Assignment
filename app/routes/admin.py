from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..schema import ProductManage, Total_data
from ..database import get_db
from ..oauth2 import get_admin_user
from ..models import User, Product

router = APIRouter(prefix="/admin", tags=["admin"])

@router.post("/products", status_code=status.HTTP_201_CREATED, response_model=ProductManage)
def add_product(product : ProductManage, db : Session = Depends(get_db), user = Depends(get_admin_user)):

    try:
        new_product = Product(**product.model_dump())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.get("/products", status_code=status.HTTP_200_OK, response_model=Total_data)
def get_total_stock(db: Session = Depends(get_db), user = Depends(get_admin_user)):
    stock = 0
    total_prod = 0
    products = db.query(Product).all()
    users = db.query(User).count()

    for prod in products:
        stock += prod.quantity
        total_prod += 1
    return {"total_stock": stock, "total_products": total_prod, "total_users": users}