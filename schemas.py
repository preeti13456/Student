from pydantic import BaseModel
from typing import Optional

class StudentCreate(BaseModel):
    name: str
    age: int
    grade: str
    address: Optional[str] = None

class StudentResponse(BaseModel):
    id: str
    name: str
    age: int
    grade: str
    address: Optional[str] = None
