from typing import Optional

from pydantic import BaseModel


class OrderBase(BaseModel):
    item: str
    quantity: int


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True


class CustomerBase(BaseModel):
    name: str
    address: str


class CreateCustomer(CustomerBase):
    pass


class Customer(BaseModel):
    id: int

    class Config:
        orm_mode = True
