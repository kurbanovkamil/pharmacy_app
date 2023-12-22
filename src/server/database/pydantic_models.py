from pydantic import BaseModel
from typing import Optional


class ModifyBaseModel(BaseModel):
    id: Optional[int] = 0


class ChangePassword(BaseModel):
    password: str


class LoginData(BaseModel):
    login: str
    password: str



class User(ModifyBaseModel):
    position: str
    login: str
    password: str
    power_level: int

class Customer(ModifyBaseModel):
    name: str
    address: str
    phone: str

class Product(ModifyBaseModel):
    name: str
    description: str
    price: float
    quantity: int

class Order(ModifyBaseModel):
    customer_id: int
    order_date: str
    total_amount: float

class OrderItem(ModifyBaseModel):
    order_id: int
    product_id: int
    quantity: int
    price: float

class Supplier(ModifyBaseModel):
    name: str
    address: str
    phone: str