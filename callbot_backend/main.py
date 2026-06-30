from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from callbot_backend.routes import rutas
from callbot_backend.database import Base, engine
import callbot_backend.db_models

app = FastAPI()

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rutas.router)

@app.get("/")
def home():
    return {"message": "API funcionando"}