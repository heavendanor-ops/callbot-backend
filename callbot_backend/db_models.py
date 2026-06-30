from sqlalchemy import Column, Integer, String
from callbot_backend.database import Base   # 👈 ruta absoluta corregida

class TransportadorDB(Base):
    __tablename__ = "transportadores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    telefono = Column(String)
