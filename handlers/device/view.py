import tornado

from db.models.device import Device
from db.models.reports import Report
from db.connection import session
from settings.template import ROOT_DIRECTORY, DEVICE


class DeviceViewHandler(tornado.web.RequestHandler):
    def get(self, id):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        device = session.query(Device).filter_by(id=id).one()
        self.render(ROOT_DIRECTORY + DEVICE['view'], device=device)