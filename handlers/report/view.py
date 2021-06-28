import tornado

from db.models.report_history import ReportHistory
from db.models.reports import Report
from db.connection import session
from settings.template import ROOT_DIRECTORY, USER, REPORT


class ReportViewHandler(tornado.web.RequestHandler):
    def get(self, report_id):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        report = session.query(Report).filter_by(id=report_id).one()
        report_history = session.query(ReportHistory).filter_by(device=report.device).all()
        self.render(ROOT_DIRECTORY + REPORT['view'],
                    id=report.id,
                    user=report.user1.name,
                    ts=report.device,
                    ts_name=report.device,
                    description=report.description,
                    urgency=report.urgency1.name,
                    status=report.status1,
                    reports_history=report_history,
                    date=report.date,
                    nakl=report.nakl)
