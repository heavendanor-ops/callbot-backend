from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from callbot_backend.routes import rutas

app = FastAPI()

# 🚨 ESTO ES CLAVE PARA FRONTEND
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción lo cambias
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(rutas.router)

@app.get("/")
def home():
    return {"message": "API funcionando"}
