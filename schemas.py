from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional
from pydantic import ConfigDict

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date
    extra_data: Optional[str] = None

class ContactCreate(ContactBase):
    pass

class ContactUpdate(ContactBase):
    pass

class ContactOut(ContactBase):
    id: int

    class Config:
        model_config = ConfigDict(from_attributes=True)  
