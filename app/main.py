from fastapi import FastAPI
from .models import Base
from .database import engine
from .routes import user, auth, product, cart


Base.metadata.create_all(engine)
app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(product.router)
app.include_router(cart.router)

@app.get("/")
async def root():
    return {"message": "BAUHINIYA Online ordering System"}

