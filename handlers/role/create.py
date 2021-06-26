import tornado

from db.models.reports import Report
from db.models.device import Device
from db.models.roles import Role
from db.models.urgencies import Urgency
from db.models.users import User
from db.connection import session
from settings.template import ROOT_DIRECTORY, ROLE


class CreateRoleHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        self.render(ROOT_DIRECTORY + ROLE['create'])

    def post(self):
        name = self.get_argument("name")
        role = Role(name=name)
        session.add(role)
        session.commit()
        self.redirect('/role/list')
