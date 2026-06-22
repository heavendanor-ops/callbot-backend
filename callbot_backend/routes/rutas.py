from fastapi import APIRouter
from callbot_backend.schemas.transportador import Transportador

router = APIRouter()

@router.post("/call")
def hacer_llamada(data: Transportador):
    respuesta = {
        "mensaje": f"Llamada procesada para {data.nombre}",
        "estado": "ok"
    }
    return respuesta