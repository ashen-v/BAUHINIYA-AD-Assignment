from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Product
from ..schema import ProductManage
from ..oauth2 import get_admin_user


router = APIRouter(prefix="/products",tags=["products"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=ProductManage)
def add_product(product : ProductManage, db : Session = Depends(get_db), user = Depends(get_admin_user)):

    try:
        new_product = Product(**product.model_dump())
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.get("/", status_code=status.HTTP_200_OK, response_model=list[ProductManage])
def view_product(db : Session = Depends(get_db)):
    try:
        products = db.query(Product).all()
        return products
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    