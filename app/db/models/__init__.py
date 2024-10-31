from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .country import Country
from .target import Target
from .target_type import TargetType
from .city import City
from .mission import Mission