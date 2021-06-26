from sqlalchemy import Column, Integer, String
from db.models.base import Base


class Urgency(Base):
    __tablename__ = 'urgencies'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(60), nullable=False)


