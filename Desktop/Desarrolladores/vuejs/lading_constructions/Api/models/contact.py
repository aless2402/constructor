from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Api.database import Base

class Contact(Base):
    __tablename__ = "contact"
    idcontactos = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    telefono = Column(String, nullable=True)
    email = Column(String, nullable=False)
    tipo_servicio = Column(String, nullable=False)
    tipo_inmueble = Column(String, nullable=True)
    presupuesto = Column(Integer, nullable=True)
    mensaje = Column(String, nullable=False)
