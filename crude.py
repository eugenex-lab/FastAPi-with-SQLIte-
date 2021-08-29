#  Date: 2021.08.26
#  Date: 2021.08.2
#  Author: eugenex

from sqlalchemy.orm import Session
import model
import schema


def get_country_by_country_id(db: Session, country_code: str):
    """
    Here we spoon countries with their ID'S
    """
    return db.query(model.Country).filter(model.Country.country_code == country_code).first()


def get_country_by_id(db: Session, sl_id: int):
    """
    This method will return single movie details based on id
    """
    return db.query(model.Country).filter(model.Country.id == sl_id).first()

def get_countries(db: Session, skip: int = 0, limit: int = 100):          #limit here na karamo, db
    """
    This method will return all movie details which are present in database
    """
    return db.query(model.Country).offset(skip).limit(limit).all()


def add_country_details_to_db(db: Session, country: schema.CountryAdd):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    """
    country_details = model.Country(
        country_code=country.country_code,
        country_name=country.country_name,
        population=country.population,
        continent=country.continent,
        fun_facts=country.fun_facts,
        country_capital=country.country_capital
    )
    db.add(country_details)
    db.commit()
    db.refresh(country_details)
    return model.Country(**country.dict())

def update_country_details(db: Session, sl_id: int, details: schema.UpdateCountry):
    """
    this method will update the database, but dnt try creating
    """
    db.query(model.Country).filter(model.Country.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.Country).filter(model.Country.id == sl_id).first()


def delete_country_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key

    """
    try:
        db.query(model.Country).filter(model.Country.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)


print ("you can crud your way to HTTP , BUt not to a womans heart looool")