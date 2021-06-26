from sqlalchemy import Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship
from db.models.base import Base
from db.models.statuses import Status
from db.models.device import Device
from db.models.urgencies import Urgency

from db.models.users import User


class Report(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True, unique=True)
    user = Column(ForeignKey('users.id'), nullable=False, index=True)
    device = Column(ForeignKey('device.id'), nullable=False, index=True)
    status = Column(ForeignKey('statuses.id'), nullable=False, index=True)
    urgency = Column(ForeignKey('urgencies.id'), nullable=False, index=True)
    description = Column(String(2000), nullable=False, server_default=text("'Описание...'"))

    user1 = relationship(User)
    status1 = relationship(Status)
    device1 = relationship(Device)
    urgency1 = relationship(Urgency)
