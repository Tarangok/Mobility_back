import tornado

from db.models.reports import Report
from db.connection import session
from settings.template import ROOT_DIRECTORY, REPORT


class ReportListHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        report_list = session.query(Report).all()
        self.render(ROOT_DIRECTORY + REPORT['list'], reports=report_list)

    def post(self):
        pass