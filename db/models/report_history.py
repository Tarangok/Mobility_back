from sqlalchemy import Integer, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from db.models.base import Base
from db.models.device import Device
from db.models.statuses import Status
from db.models.urgencies import Urgency
from db.models.users import User


class ReportHistory(Base):
    __tablename__ = 'report_history'

    id = Column(Integer, primary_key=True, unique=True)
    report_id = Column(ForeignKey('reports.id'), nullable=False, index=True)
    status = Column(ForeignKey('statuses.id'), nullable=False, index=True)
    user = Column(ForeignKey('users.id'), index=True)
    device = Column(ForeignKey('device.id'), index=True)
    urgency = Column(ForeignKey('urgencies.id'), index=True)
    description = Column(String(2000), index=True)
    date = Column(DateTime, nullable=False)

    device1 = relationship('Device')
    report1 = relationship('Report')
    status1 = relationship('Status')
    urgency1 = relationship('Urgency')
    user1 = relationship('User')
