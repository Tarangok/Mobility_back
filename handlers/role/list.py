import tornado

from db.models.reports import Report
from db.connection import session
from db.models.roles import Role
from settings.template import ROOT_DIRECTORY, ROLE


class RoleListHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        roles = session.query(Role).all()
        self.render(ROOT_DIRECTORY + ROLE['list'], roles=roles, user_role=self.get_cookie("role"))

    def post(self):
        pass