import tornado

from db.models.users import User
from db.connection import session
from settings.template import ROOT_DIRECTORY, USER


class UserListHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        users = session.query(User).all()
        self.render(ROOT_DIRECTORY + USER['list'], users=users, user_role=self.get_cookie("role"))