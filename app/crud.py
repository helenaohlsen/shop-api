from random import random

from sqlalchemy.orm import Session

import models
import schemas


def get_all_orders(db: Session):
    return db.query(models.Order).all()


def create_order(db: Session, order: schemas.OrderCreate, user_id: int):
    db_order = models.Order(item=order.item, quantity=order.quantity, customer_id=user_id)
    db.add(db_order)
    db.commit()
    return db_order


def get_order_by_id(db: Session, order_id: int):
    return db.query(models.Order).filter(models.Order.id == order_id).first()


def delete_order(db: Session, order_id: int):
    order_query = db.query(models.Order).filter(models.Order.id == order_id)
    order_query.delete()
    db.commit()


def update_order(db: Session, updated_order: schemas.OrderBase, order_id: int):
    order_query = db.query(models.Order).filter(models.Order.id == order_id)
    order_query.update(updated_order.dict())


def get_customer_by_name(db: Session, name: str):
    return db.query(models.Customer).filter(models.Customer.name == name).first()


def get_customer_by_id(db: Session, cust_id: int):
    return db.query(models.Customer).filter(models.Customer.id == cust_id).first()


def get_all_customers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Customer).offset(skip).limit(limit).all()


def create_customer(db: Session, customer: schemas.CreateCustomer):
    db_customer = models.Customer(name=customer.name, address=customer.address)
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


def cancel_all_customer_orders(db: Session, customer_id: int):
    order_query = db.query(models.Order).filter(models.Order.customer_id == customer_id)
    order_query.delete()
    db.commit()
