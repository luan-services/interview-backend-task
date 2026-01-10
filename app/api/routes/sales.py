from fastapi import APIRouter, HTTPException
from sqlmodel import select
from typing import List
from app.config.database import SessionDep
from app.models.sale import Sale

# https://fastapi.tiangolo.com/tutorial/bigger-applications/#another-module-with-apirouter

router = APIRouter(prefix="/sales", tags=["sales"])

@router.get("/", response_model=List[Sale])
async def read_sales(session: SessionDep):
    return session.exec(select(Sale)).all()

@router.post("/", response_model=Sale)
async def create_sale(sale: Sale, session: SessionDep):
    session.add(sale)
    session.commit()
    session.refresh(sale)
    return sale

@router.put("/{sale_id}", response_model=Sale)
async def update_sale(sale_id: int, sale_data: Sale, session: SessionDep):
    sale = session.get(Sale, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale Not Found")
    
    input_data = sale_data.model_dump(exclude_unset=True)
    sale.sqlmodel_update(input_data)
    
    session.add(sale)
    session.commit()
    session.refresh(sale)
    return sale

@router.delete("/{sale_id}")
async def delete_sale(sale_id: int, session: SessionDep):
    sale = session.get(Sale, sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale Not Found")
    session.delete(sale)
    session.commit()
    return {"message": "Sale Deleted"}