import tornado.ioloop
import tornado.web

from handlers.report.create import CreateReportHandler
from handlers.report.list import ReportListHandler
from handlers.report.view import ReportViewHandler
from handlers.role.create import CreateRoleHandler
from handlers.role.list import RoleListHandler
from handlers.role.view import RoleViewHandler
from handlers.root import RootHandler
from handlers.device.create import CreateDeviceHandler
from handlers.device.list import DeviceListHandler
from handlers.device.view import DeviceViewHandler
from handlers.user.auth import UserAuthHandler
from handlers.user.create import CreateUserHandler
from handlers.user.list import UserListHandler
from handlers.user.logout import UserLogoutHandler
from handlers.user.view import UserViewHandler

from settings.app import APPLICATION

def make_app():
    return tornado.web.Application([
        (r"/user/create", CreateUserHandler),
        (r"/user/list", UserListHandler),
        (r"/user/(\d+$)", UserViewHandler),
        (r"/user/auth", UserAuthHandler),
        (r"/user/logout", UserLogoutHandler),

        (r"/role/create", CreateRoleHandler),
        (r"/role/list", RoleListHandler),
        (r"/role/(\d+$)", RoleViewHandler),

        (r"/report/create", CreateReportHandler),
        (r"/report/list", ReportListHandler),
        (r"/report/(\d+$)", ReportViewHandler),

        (r"/device/create", CreateDeviceHandler),
        (r"/device/list", DeviceListHandler),
        (r"/device/(\d+$)", DeviceViewHandler),
        (r"/", UserAuthHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(address=APPLICATION['url'], port=APPLICATION['port'])
    print(f"Start server on {APPLICATION['url']}:{APPLICATION['port']}")
    tornado.ioloop.IOLoop.current().start()

