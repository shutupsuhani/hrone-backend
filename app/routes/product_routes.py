from fastapi import APIRouter, Query
from typing import List, Optional
from app.database import db
from app.models.product import ProductIn, ProductOut
from pymongo import ASCENDING

router = APIRouter()

@router.post("/create", status_code=201, response_model=ProductOut)
async def create_product(product: ProductIn):
    result = await db.products.insert_one(product.dict())
    product_dict = product.dict()
    product_dict["_id"] = str(result.inserted_id)
    return product_dict


@router.get("/find", response_model=List[ProductOut])
async def get_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    
    if name:
        query["name"] = name
    
    if size:
        query["sizes"] = {"$elemMatch": {"size": size}}

    cursor = db.products.find(query).skip(offset).limit(limit).sort("name", ASCENDING)
    results = await cursor.to_list(length=limit)

    # convert ObjectId to str
    for product in results:
        product["_id"] = str(product["_id"])
    
    return results