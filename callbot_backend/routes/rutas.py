from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from callbot_backend.db_models import TransportadorDB
from schemas.transportador import Transportador


from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def prueba():
    return {"ok": True}




# Crear sesión de DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ✅ Crear transportador
@router.post("/transportador/")
def crear_transportador(t: Transportador, db: Session = Depends(get_db)):
    nuevo = TransportadorDB(
        nombre=t.nombre,
        telefono=t.telefono
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return {"mensaje": "Guardado", "id": nuevo.id}


# ✅ Listar transportadores
@router.get("/transportadores/")
def listar_transportadores(db: Session = Depends(get_db)):
    datos = db.query(TransportadorDB).all()
    return datos