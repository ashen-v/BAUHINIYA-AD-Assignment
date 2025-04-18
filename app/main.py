from fastapi import FastAPI
from .models import Base
from .database import engine
from .routes import user


Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "BAUHINIYA Online ordering System"}

