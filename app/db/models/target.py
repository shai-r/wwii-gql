from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.models import Base

class Target(Base):
   __tablename__ = "targets"
   target_id = Column(Integer, primary_key=True, autoincrement=True)
   mission_id = Column(Integer, ForeignKey('missions.mission_id'))
   city_id = Column(Integer, ForeignKey('cities.city_id'))
   target_type_id = Column(Integer, ForeignKey('target_types.target_type_id'))
   target_priority = Column(Integer)

   mission = relationship("Mission", back_populates="targets")
   city = relationship("City", back_populates="targets")
   target_types = relationship("TargetType", back_populates="targets")