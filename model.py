#  Date: 2021.08.26
#  Author: eugenex

from sqlalchemy import Boolean, Column, Integer, String
from sql_engine import Base

#  HERE WE
class Country(Base):
    __tablename__ = "country"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False) #test with or withouto increatment to see change levels
    country_code = Column(String, unique=True, index=True, nullable=False)   ###### WHAT IS NULLABLE = TRUE OR FALSE AND INDEX
    country_name = Column(String(255),unique=True, index=True, nullable=False)
    population = Column(Integer, index=True, nullable=False)
    continent = Column(String, index=True, nullable=False)
    fun_facts: str = Column(String, nullable=False)
    country_capital = Column(String, index=True)


print("model is an abstraction of reality")
