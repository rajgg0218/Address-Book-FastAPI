from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine
import math

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/addresses", response_model=schemas.AddressResponse)
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)


@app.get("/addresses", response_model=list[schemas.AddressResponse])
def get_addresses(db: Session = Depends(get_db)):
    return crud.get_addresses(db)


@app.put("/addresses/{address_id}", response_model=schemas.AddressResponse)
def update_address(address_id: int, address: schemas.AddressUpdate, db: Session = Depends(get_db)):
    result = crud.update_address(db, address_id, address)

    if not result:
        raise HTTPException(status_code=404, detail="Address not found")

    return result


@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    result = crud.delete_address(db, address_id)

    if not result:
        raise HTTPException(status_code=404, detail="Address not found")

    return {"message": "Address deleted"}