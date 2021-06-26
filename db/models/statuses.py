from sqlalchemy import Column, Integer, String
from db.models.base import Base


class Status(Base):
    __tablename__ = 'statuses'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(60), nullable=False)


