import tornado
from db.models.reports import Report
from db.connection import session
from db.models.roles import Role
from settings.template import ROOT_DIRECTORY, ROLE


class RoleViewHandler(tornado.web.RequestHandler):
    def get(self, id):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        role = session.query(Role).filter_by(id=id).one()
        self.render(ROOT_DIRECTORY + ROLE['view'], role=role)