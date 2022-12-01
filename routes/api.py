from fastapi import APIRouter
from src.endpoints.product import product_ep as product

router = APIRouter()
router.include_router(product.router)
