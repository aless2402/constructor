from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Api.database import get_db
from models.contact import Contact
from services.contact import create_contact
from schemas.contact import ContactCreate

router = APIRouter()

@router.post("/contact", response_model=ContactCreate)
def enviar_contacto(contact: ContactCreate, db: Session = Depends(get_db)):
    try:
        return create_contact(db=db, contact=contact)
    except Exception as e:
        raise HTTPException(status_code=400, detail="Error al enviar el contacto.")
