from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from db.models.base import Base
from db.models.users import User

class UserAuth(Base):
    __tablename__ = 'user_auth'

    user_login = Column(String(100), primary_key=True, unique=True)
    user_id = Column(ForeignKey('users.id'), nullable=False, index=True)
    password = Column(String(2048), nullable=False)

    user = relationship(User)
