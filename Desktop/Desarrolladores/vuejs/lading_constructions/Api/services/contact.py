from sqlalchemy.orm import Session
from models.contact import Contact
from schemas.contact import ContactCreate

def create_contact(db: Session, contact: ContactCreate):
    nuevo_contacto = Contact(
        nombre=contact.nombre,
        apellido=contact.apellido,
        telefono=contact.telefono,
        email=contact.email,
        tipo_servicio=contact.tipo_servicio,
        tipo_inmueble=contact.tipo_inmueble,
        presupuesto=contact.presupuesto,
        mensaje=contact.mensaje
    )
    db.add(nuevo_contacto)
    db.commit()
    db.refresh(nuevo_contacto)
    return nuevo_contacto
