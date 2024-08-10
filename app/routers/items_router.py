from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

data = {
    1: {
        "uid": "EVaHDz",
        "name": "Product 01",
        "price": 100,
        "quantity": 10
    },
    2: {
        "uid": "IrkQyu",
        "name": "Product 02",
        "price": 1000,
        "quantity": 2
    },
    3: {
        "uid": "9leaUq",
        "name": "Product 03",
        "price": 150,
        "quantity": 15
    }
}


@router.get("")
async def get_products():
    return data


@router.get("/{product_id}")
async def get_product(product_id: int):
    if product_id not in data:
        raise HTTPException(status_code=404, detail="Product not found")
    return data[product_id]
