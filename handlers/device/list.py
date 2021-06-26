import tornado

from db.models.device import Device
from db.models.reports import Report
from db.connection import session
from settings.template import ROOT_DIRECTORY, DEVICE


class DeviceListHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        devices = session.query(Device).all()
        self.render(ROOT_DIRECTORY + DEVICE['list'], devices=devices, user_role=self.get_cookie("role"))

    def post(self):
        pass