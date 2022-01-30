from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, unique=True)
    item = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    customer_id = Column(Integer, ForeignKey("customers.id"))
