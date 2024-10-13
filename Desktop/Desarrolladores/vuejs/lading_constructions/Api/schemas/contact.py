from pydantic import BaseModel, EmailStr
from typing import Optional

class ContactCreate(BaseModel):
    nombre: str
    apellido: str
    telefono: Optional[str]
    email: EmailStr
    tipo_servicio: str
    tipo_inmueble: Optional[str]
    presupuesto: Optional[int]
    mensaje: str
