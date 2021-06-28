import datetime

import tornado

from db.models.report_history import ReportHistory
from db.models.reports import Report
from db.models.device import Device
from db.models.urgencies import Urgency
from db.models.users import User
from db.connection import session

from settings.template import ROOT_DIRECTORY, REPORT


class CreateReportHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("auth") != "true":
            self.redirect("/")

        user_id = int(self.get_cookie("uid"))
        devices = session.query(Device).all()
        urgencies = session.query(Urgency).all()
        user = session.query(User).filter(User.id == user_id).one()

        self.render(ROOT_DIRECTORY + REPORT['create'],
                    devices=devices,
                    urgencies=urgencies,
                    user=user)

    def post(self):
        user_id = int(self.get_cookie("uid"))
        device = self.get_argument("device")
        urgency = self.get_argument("urgency")
        description = self.get_argument("description")
        nakl = self.get_argument("nakl")
        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        report = Report(user=user_id, device=device, urgency=urgency, description=description, status=1, date=date, nakl=nakl)

        session.add(report)
        session.commit()

        report_history = ReportHistory(report_id=report.id, status=report.status, user=report.user, urgency=urgency,
                                       device=report.device, description=description, date=date)
        session.add(report_history)
        session.commit()
        self.redirect('/report/list')

