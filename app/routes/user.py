from fastapi import HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schema import Register
from ..utils import hash

router = APIRouter(prefix="/register", tags=["register"])

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Register)
def register(user: Register, db: Session = Depends(get_db)):
    try:
        user.password = hash(user.password)
        new_user = User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
