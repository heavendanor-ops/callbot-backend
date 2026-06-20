from database import engine, Base
from routes.rutas import router
from callbot_backend.routes.rutas import router

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
def inicio():
    return {"mensaje": "Servidor listo 🚀"}
