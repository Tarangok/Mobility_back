import tornado

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
        devices = session.query(Device).all()
        urgencies = session.query(Urgency).all()
        users = session.query(User).all()

        self.render(ROOT_DIRECTORY + REPORT['create'],
                    devices=devices,
                    urgencies=urgencies,
                    users=users)

    def post(self):
        user_id = self.get_argument("user")
        device = self.get_argument("device")
        urgency = self.get_argument("urgency")
        description = self.get_argument("description")
        report = Report(user=user_id, device=device, urgency=urgency, description=description, status=1)
        session.add(report)
        session.commit()
        self.redirect('/report/list')

