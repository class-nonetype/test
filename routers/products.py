from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix = '/products',
    tags = ['Products'],
    responses = {
        404 : {'message': 'Not found!'}
    }
)


class Product(BaseModel):
    id : int
    name : str 
    description : str | None = None
    stock : int
    price : int

products = [
    Product(id = 0, name = 'Product 0', description = 'Product 0 description', stock = 10, price = 1990),
    Product(id = 1, name = 'Product 1', description = 'Product 1 description', stock = 20, price = 21990),
    Product(id = 2, name = 'Product 2', description = 'Product 2 description', stock = 30, price = 31990),
    Product(id = 3, name = 'Product 3', description = 'Product 3 description', stock = 40, price = 51990),
    Product(id = 4, name = 'Product 4', description = 'Product 4 description', stock = 50, price = 71990),
    Product(id = 5, name = 'Product 5', description = 'Product 5 description', stock = 60, price = 91990),
    Product(id = 6, name = 'Product 6', description = 'Product 6 description', stock = 70, price = 61990),
    Product(id = 7, name = 'Product 7', description = 'Product 7 description', stock = 80, price = 61990),

]
@router.get("/")
async def get_products():
    return products


@router.get("/{id}")
async def get_product_by_id(id: int):
    return products[id]

