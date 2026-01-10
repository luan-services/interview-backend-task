from fastapi import APIRouter, HTTPException
from sqlmodel import select
from typing import List
from app.config.database import SessionDep
from app.models.product import Product


# https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=List[Product])
async def read_products(session: SessionDep):
    return session.exec(select(Product)).all()

@router.post("/", response_model=Product)
async def create_product(product: Product, session: SessionDep):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.put("/{product_id}", response_model=Product)
async def update_product(product_id: int, product_data: Product, session: SessionDep):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found")
    
    input_data = product_data.model_dump(exclude_unset=True)
    product.sqlmodel_update(input_data)
    
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

@router.delete("/{product_id}")
async def delete_product(product_id: int, session: SessionDep):
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product Not Found")
    session.delete(product)
    session.commit()
    return {"message": "Product Deleted"}