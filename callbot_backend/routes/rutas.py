from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from callbot_backend.database import engine, Base
from callbot_backend.db_models import TransportadorDB
from schemas.transportador import Transportador

router = APIRouter()

@router.post("/call")
def hacer_llamada(data: Transportador):

    respuesta = {
        "mensaje": f"Llamada procesada para {data.nombre}",
        "estado": "ok"
    }

    return respuesta
