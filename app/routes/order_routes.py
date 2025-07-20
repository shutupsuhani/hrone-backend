from fastapi import APIRouter, Path, Query
from app.database import db
from app.models.order import OrderIn, OrderOut
from datetime import datetime
from typing import List
from bson import ObjectId

router = APIRouter()

@router.post("/create-order", status_code=201, response_model=OrderOut)
async def create_order(order: OrderIn):
    order_data = order.dict()
    result = await db.orders.insert_one(order_data)
    return {"id": str(result.inserted_id)}


@router.get("/find/{user_id}", response_model=List[OrderOut])
async def get_orders(user_id: str):
    orders_cursor = db.orders.find({"userId": user_id})
    orders = await orders_cursor.to_list(length=100)
    for order in orders:
        order["id"] = str(order["_id"])  
    return orders