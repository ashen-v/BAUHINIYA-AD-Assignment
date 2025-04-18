from fastapi import FastAPI
from .models import Base
from .database import engine
from .routes import user
from .routes import auth

Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "BAUHINIYA Online ordering System"}

