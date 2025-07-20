from pydantic import BaseModel
from typing import List

class OrderItem(BaseModel):
    productId: str
    qty: int

class OrderIn(BaseModel):
    userId: str
    items: List[OrderItem]

class OrderOut(BaseModel):
    id: str
    userId: str  
    items: List[OrderItem]