from fastapi import APIRouter,Depends
from schemas.product import ShowProduct,CreateProduct,BaseProduct
from sqlalchemy.orm import Session
from models.product import Product
from database import get_db
from typing import List

router = APIRouter()

@router.get('/products',response_model=List[ShowProduct])
def products_list(db: Session = Depends(get_db)):
    products=db.query(Product).all()
    return products


@router.post('/save_products',response_model=CreateProduct)
def save_roduct(form:CreateProduct,db: Session = Depends(get_db)):
    db_product = Product(name=form.name,price=form.price,count=form.count)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.put('/product/{id}',response_model=ShowProduct)
def update_product(id : int,db:Session=Depends(get_db)):
    db_product =db.query(Product).filter(Product.id == id).first()
    if db_product:
        # db_product.name = 
        pass
    return db_product