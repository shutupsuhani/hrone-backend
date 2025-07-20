from pydantic import BaseModel, Field
from typing import List

class Size(BaseModel):
    size: str
    quantity: int

class ProductIn(BaseModel):
    name: str
    price: float
    sizes: List[Size]

class ProductOut(ProductIn):
    id: str = Field(alias="_id")
