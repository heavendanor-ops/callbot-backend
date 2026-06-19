from fastapi import APIRouter
from schemas.transportador import Transportador

router = APIRouter()

@router.post("/call")
def hacer_llamada(data: Transportador):
    
    # Aquí puedes usar tu lógica real
    respuesta = {
        "mensaje": f"Llamada procesada para {data.nombre}",
        "estado": "ok"
    }
    
    return respuesta
