from database import Base
from sqlalchemy import Column,String,Integer

class Product(Base):
    __tablename__ = "Product"

    id = Column(Integer,primary_key=True)
    name = Column(String,)
    price = Column(Integer,)
    count = Column(Integer)