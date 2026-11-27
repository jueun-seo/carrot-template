from fastapi import APIRouter
from schemas import ProductOut
from deps import SessionDep
from models import Product
from sqlalchemy import select

router = APIRouter(prefix='/api/products', tags=['products'])

@router.get('', response_model=list[ProductOut])
def list_products(db: SessionDep):
  return db.scalars(select(Product)).all()
