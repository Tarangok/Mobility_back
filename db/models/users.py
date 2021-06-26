from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.exc import NoResultFound
from db.connection import session
from db.models.base import Base
from db.models.roles import Role

class User(Base):
    ADMIN = 1
    WORKSHOP = 2
    LABORATORY = 3
    TSC = 4
    MANUFACTURER = 5

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(60))
    role = Column(ForeignKey('roles.id'), nullable=False, index=True)

    role1 = relationship(Role)

    @classmethod
    def get_user_role(cls, id):
        user = cls.get_user_by_id(id)
        if user:
            return user.role
        else:
            return None

    @classmethod
    def get_user_by_id(cls, id):
        try:
            user = session.query(cls).filter(cls.id == id).one()
        except NoResultFound:
            return None
        return user

