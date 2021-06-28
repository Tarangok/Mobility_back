import tornado
from sqlalchemy import desc

from db.models.reports import Report
from db.connection import session
from settings.template import ROOT_DIRECTORY, REPORT


class ReportListHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        report_list = session.query(Report).order_by(Report.status==10).all()
        self.render(ROOT_DIRECTORY + REPORT['list'], reports=report_list, role=self.get_cookie("role"))

    def post(self):
        pass