#  Date: 2021.08.26
#  Author: eugenex

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud
import model
import schema
from sql_engine import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

# initiating app
app = FastAPI(
    title="Country Details",
    description="You can perform CRUD operation by using MY API",
    version="0.0.1"
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/countries_details', response_model=List[schema.Country])      #END POINT
def countries_details(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = crud.get_countries(db=db, skip=skip, limit=limit)
    return countries


@app.post('/input_countries', response_model=schema.CountryAdd)
def input_countries(country: schema.CountryAdd, db: Session = Depends(get_db)):
    country_code = crud.get_country_by_country_id(db=db, country_code=country.country_code)
    if country_code:
        raise HTTPException(status_code=400, detail=f"Country code {country.country_code} already exist in our database: {country_code}")
    return crud.add_country_details_to_db(db=db, country=country)


@app.delete('/purge_country_by_id')
def purge_country_by_id(sl_id: int, db: Session = Depends(get_db)):
    details = crud.get_country_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No country Id found in the database to delete")

    try:
        crud.delete_country_details_by_id(db=db, sl_id=sl_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete specified country in the db: {e}")
    return {"delete status": "record delete successful"}


@app.put('/update_country_details', response_model=schema.Country)
def update_movie_details(sl_id: int, update_param: schema.UpdateCountry, db: Session = Depends(get_db)):
    details = crud.get_country_by_id(db=db, sl_id=sl_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found in the country database to update")

    return crud.update_country_details(db=db, details=update_param, sl_id=sl_id)


print("Here we deploy the app, if app is application , then we can say its subtle apply")