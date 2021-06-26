import tornado

from db.models.roles import Role
from db.models.user_auth import UserAuth
from db.models.users import User
from db.connection import session
from settings.template import ROOT_DIRECTORY, USER


class CreateUserHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("auth") == "true":
            role = User.get_user_role(int(self.get_cookie("uid")))
        else:
            role = None
            self.redirect("/")
        if role == 1:
            roles_list = session.query(Role).all()
            self.render(ROOT_DIRECTORY + USER['create'], roles=roles_list)
        else:
            self.write("Permission denied")


    def post(self):
        name = self.get_argument("name")
        login = self.get_argument("login")
        role = self.get_argument("role")
        password = self.get_argument("password")
        user = User(name=name, role=role)

        session.add(user)
        session.commit()
        user_auth = UserAuth(user_id=user.id, password=password, user_login=login)
        session.add(user_auth)
        session.commit()
        self.redirect('/user/list')