from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .models import User
from .database import get_db


SECRET_KEY = "WmqbDCyUBDaGRJJcc6NbPxG2ihig6US2AieqB3B6dM28DBcFXx9J38djBNG3"
ALGORITHEM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 60

def create_acess_token(data: dict):

    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHEM)
    return encoded_jwt