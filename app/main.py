from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth, sessions

Base.metadata.create_all(bind=engine)

app = FastAPI(title="BJJ Training Log")

app.include_router(auth.router)
app.include_router(sessions.router)

@app.get("/")
def root():
    return {"message": "BJJ Training Log API"}