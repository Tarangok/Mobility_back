from sqlalchemy import Column, Integer, String
from db.models.base import Base
from db.connection import session

class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(60), nullable=False)

    @classmethod
    def add_new_role(cls, role_name):
        try:
            new_role = session.query(cls).filter(name=role_name).one()
            return None
        except:
            new_role = Role(name=role_name)
            session.commit()
            session.add()
            return new_role


