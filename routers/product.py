from fastapi import APIRouter

router = APIRouter()

@router.get('/products')
def products_list():
    return "ok"