from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..utils import verify
from ..oauth2 import create_acess_token, get_current_user


router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(user_cred: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == user_cred.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="invalid credentials")
    
    if not verify(user_cred.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="invalid credentials")
    
    acess_token = create_acess_token({"user_id": user.id})
    
    return {"token_type": "Bearer", "access_token": acess_token}

@router.get("/me")
def read_users_me(user: User = Depends(get_current_user)):
    return user