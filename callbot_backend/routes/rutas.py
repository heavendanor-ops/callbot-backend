from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from callbot_backend.database import get_db

router = APIRouter()

@router.post("/call")
def hacer_llamada(data: Transportador):
    
    # Aquí puedes usar tu lógica real
    respuesta = {
        "mensaje": f"Llamada procesada para {data.nombre}",
        "estado": "ok"
    }
    
    return respuesta
