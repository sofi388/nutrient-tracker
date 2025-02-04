from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base 

Base = declarative_base() # setting up the base class for SQLAlchemy ORM (Object-Relational Mapping) models

class NutrientIntake(Base):
    __tablename__ = 'nutrient_intake'

    id = Column(Integer, primary_key=True, autoincrement=True)
    age_low = Column(Integer, nullable=False)
    age_high = Column(Integer, nullable=False)
    male_low_activity = Column(Integer, nullable=False)
    male_moderate_activity = Column(Integer, nullable=False)
    male_high_activity = Column(Integer, nullable=False)
    female_low_activity = Column(Integer, nullable=False)
    female_moderate_activity = Column(Integer, nullable=False)
    female_high_activity = Column(Integer, nullable=False)