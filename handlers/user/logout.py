import tornado


class UserLogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_cookie("uid")
        self.clear_cookie("auth")
        self.clear_cookie("role")
        self.redirect("/")

    def post(self):
        pass