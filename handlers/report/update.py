import datetime

import tornado

from db.models.report_history import ReportHistory
from db.models.reports import Report
from db.models.device import Device
from db.models.urgencies import Urgency
from db.models.users import User
from db.connection import session

from settings.template import ROOT_DIRECTORY, REPORT


class ReportUpdateHandler(tornado.web.RequestHandler):
    def get(self):
        pass

    def post(self):
        report_id = self.get_argument("report_id")
        # status_id = self.get_argument("status_id")
        action = self.get_argument("action")
        new_descr = self.get_argument("status_send")

        report = Report.get_report_by_id(report_id)

        if action == "send":
            report.status += 1
        elif action == "get":
            report.status += 1
        elif action == "not_repair":
            report.status = 8
        elif action == "repair":
            report.status = 7
        elif action == "send_lab":
            report.status = 9
        elif action == "send_ceh":
            report.status = 10
        elif action == "repair_in_lab":
            report.status = 11
        elif action == "repair_in_tsc":
            report.status = 12
        report.description = new_descr
        session.commit()


        date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        report_history = ReportHistory(report_id=report.id, status=report.status, user=report.user,
                                       urgency=report.urgency, description=new_descr,
                                       device=report.device, date=date)
        session.add(report_history)
        session.commit()
        if action == "get":
            self.redirect(f'/report/{report.id}')
        elif action == "repair_in_lab":
            self.redirect(f'/report/{report.id}')
        elif action == "repair_in_lab":
            self.redirect(f'/report/{report.id}')
        else:
            self.redirect('/report/list')

