from sqlalchemy import Column, Integer, String
from db.models.base import Base




class Place(Base):
    __tablename__ = 'places'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(60), nullable=False)


