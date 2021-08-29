#  Date: 2021.08.26
#  Author: eugenex

from typing import Optional
from pydantic import BaseModel


class CountryBase(BaseModel):
    country_name: str
    population: str
    country_capital: str

class CountryAdd(CountryBase):
    country_code: str
    continent:str
    fun_facts: str
    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class Country(CountryAdd):
    id: int

    # Behaviour of pydantic can be controlled via the Config class on a model
    class Config:
        orm_mode = True


class UpdateCountry(BaseModel):
    # Optional[str] is just a shorthand or alias for Union[str, None].
    fun_facts: str
    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True

print("in the grandscheme of thing we are insignificant, lllolllll")