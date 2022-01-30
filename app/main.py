from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import models
import schemas
from db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/orders/", response_model=list[schemas.Order])
def read_orders(db: Session = Depends(get_db)):
    orders = crud.get_all_orders(db)
    return orders


@app.post("/orders/", response_model=schemas.Order)
def create_order(
        order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order=order, user_id=101)

