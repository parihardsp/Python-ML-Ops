from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description

# Initialize FastAPI
app = FastAPI()


# Defining data model for Order and Product
class Order(BaseModel):
    product: str
    units: int


class Product(BaseModel):
    name: str
    notes: str


@app.get("/start")
async def start_endpoint():
    return {"message": "Hello! World"}


@app.get("/hello")
async def hello_endpoint(name: str = 'World'):
    return {"message": f"Hello, {name}!"}


@app.post("/orders")
async def place_order(product: str, units: int):
    """
    :param product:
    :param units:
    :return:
    """
    return {"message": f"Your Orders for {units} {product} has been placed successfully!"}


@app.post("/orders-pydantic")
async def place_order(order: Order):
    return {"message": f"Your Orders for {order.units} {order.product} has been placed successfully!"}


@app.post("/product-description")
async def product_desc(product: Product):
    description = generate_description(f"Product Name: {product.name}, Notes: {product.notes}")
    return {"product_description": description}
