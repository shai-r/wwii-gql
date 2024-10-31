from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from app.db.models import Base

class Country(Base):
   __tablename__ = "countries"
   country_id = Column(Integer, primary_key=True, autoincrement=True)
   country_name = Column(String)

   cities = relationship(
       "City",
       back_populates="country",
       cascade="all, delete-orphan"
   )