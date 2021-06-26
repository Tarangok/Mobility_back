import tornado
from settings.template import USER, ROOT_DIRECTORY
from db.models.users import User
from db.connection import session


class UserViewHandler(tornado.web.RequestHandler):
    def get(self, id):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        user = session.query(User).filter_by(id=id).one()
        self.render(ROOT_DIRECTORY + USER['view'],
                    user=user)

    def post(self):
        pass