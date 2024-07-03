from pydantic import BaseModel


class BaseProduct(BaseModel):
    name:str

class ShowProduct(BaseProduct):
    price : int

class CreateProduct(BaseProduct):
    count : int
    price : int