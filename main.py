# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import engine, SessionLocal
from swagger_config import OPENAPI_KWARGS

models.Base.metadata.create_all(bind=engine)

app = FastAPI(**OPENAPI_KWARGS)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/contacts/", response_model=schemas.ContactOut, tags=["Contacts"])
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db=db, contact=contact)

@app.get("/contacts/", response_model=list[schemas.ContactOut], tags=["Contacts"])
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_contacts(db, skip=skip, limit=limit)

@app.get("/contacts/{contact_id}", response_model=schemas.ContactOut, tags=["Contacts"])
def read_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.get_contact(db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@app.put("/contacts/{contact_id}", response_model=schemas.ContactOut, tags=["Contacts"])
def update_contact(contact_id: int, contact: schemas.ContactUpdate, db: Session = Depends(get_db)):
    db_contact = crud.update_contact(db, contact_id=contact_id, contact=contact)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@app.delete("/contacts/{contact_id}", response_model=schemas.ContactOut, tags=["Contacts"])
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    db_contact = crud.delete_contact(db, contact_id=contact_id)
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact

@app.get("/contacts/search/", response_model=list[schemas.ContactOut], tags=["Search"])
def search_contacts(first_name: str | None = None, last_name: str | None = None, email: str | None = None, db: Session = Depends(get_db)):
    return crud.search_contacts(db, first_name=first_name, last_name=last_name, email=email)

@app.get("/contacts/upcoming_birthdays/", response_model=list[schemas.ContactOut], tags=["Search"])
def upcoming_birthdays(db: Session = Depends(get_db)):
    return crud.get_upcoming_birthdays(db)
