from fastapi import APIRouter, Depends
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..database import get_db
from ..oauth2 import get_current_user
from ..models import Product

router = APIRouter(tags=["html"])

templates = Jinja2Templates(directory="app/templates")

@router.get("/logins", response_class=HTMLResponse)
def get_login_page(request: Request):
    return templates.TemplateResponse("logins.html", {"request": request})

@router.get("/products", response_class=HTMLResponse)
def get_product_page(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return templates.TemplateResponse("products.html", {"request": request,  "products": products})

@router.get("/registers", response_class=HTMLResponse)
def get_register_page(request: Request):
    return templates.TemplateResponse("registers.html", {"request": request})

@router.get("/carts", response_class=HTMLResponse)
def get_cart_page(request: Request):
    return templates.TemplateResponse("carts.html", {"request": request})

@router.get("/checkouts", response_class=HTMLResponse)
def get_checkout_page(request: Request):
    return templates.TemplateResponse("checkout.html", {"request": request})