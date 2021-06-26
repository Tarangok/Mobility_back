import tornado

from db.connection import session
from db.models.user_auth import UserAuth
from db.models.users import User
from sqlalchemy import and_
from sqlalchemy.exc import NoResultFound

from settings.template import ROOT_DIRECTORY, USER

class UserAuthHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(ROOT_DIRECTORY + USER['auth'], error=" ", text="text-black-50")

    def post(self):
        user_login = self.get_argument("login")
        password = self.get_argument("password")
        try:
            user = session.query(UserAuth).filter(and_(
                UserAuth.user_login == user_login,
                UserAuth.password == password
            )).one()
        except NoResultFound:
            self.set_cookie("auth", "false")
            self.render(ROOT_DIRECTORY + USER['auth'], error="Неверный логин или пароль!", text="text-danger")

        role = User.get_user_role(user.user_id)
        self.set_cookie("auth", "true")
        self.set_cookie("uid", str(user.user_id))
        self.set_cookie("role", str(role))
        self.redirect('/report/list')