import tornado

from db.models.reports import Report
from db.models.device import Device
from db.models.urgencies import Urgency
from db.models.users import User
from db.connection import session
from settings.template import ROOT_DIRECTORY, DEVICE


class CreateDeviceHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        self.render(ROOT_DIRECTORY + DEVICE['create'])

    def post(self):
        name = self.get_argument("name")
        device = Device(name=name)
        session.add(device)
        session.commit()
        self.redirect('/device/list')