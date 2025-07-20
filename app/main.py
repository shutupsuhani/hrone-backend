# main.py

from fastapi import FastAPI
from app.routes import product_routes, order_routes

app = FastAPI()

app.include_router(product_routes.router,prefix='/products')
app.include_router(order_routes.router,prefix='/orders')

@app.get("/")
async def root():
    return {"message": "Ecommerce API is running!"}