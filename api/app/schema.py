from pydantic import BaseModel

class Course(BaseModel):
    name: str
    price: float
