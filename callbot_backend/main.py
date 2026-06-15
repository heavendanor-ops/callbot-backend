from database import engine, Base
from routes.rutas import router
from callbot_backend.routes.rutas import router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def inicio():
    return {"mensaje": "Servidor listo 🚀"}
