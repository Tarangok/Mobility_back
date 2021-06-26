import tornado
from db.models.reports import Report
from db.connection import session
from settings.template import ROOT_DIRECTORY, USER


class ReportViewHandler(tornado.web.RequestHandler):
    def get(self, report_id):
        if self.get_cookie("auth") != "true":
            self.redirect("/")
        report = session.query(Report).filter_by(id=report_id).one()
        self.render(ROOT_DIRECTORY + USER['view'],
                    user=report.user1.fio,
                    ts=report.ts,
                    ts_name=report.ts1.name,
                    description=report.description,
                    urgency=report.urgency1.name,
                    status=report.status1.name)
