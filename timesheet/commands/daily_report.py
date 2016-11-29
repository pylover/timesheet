# -*- coding: utf-8 -*-
from timesheet.commands import Command
from timesheet.models import DBSession, Task
from prettytable import PrettyTable
from datetime import timedelta, datetime
from sqlalchemy import func

__author__ = 'vahid'


class DailyReportCommand(Command):
    name = 'daily-report'
    description = 'Print daily report'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('days', nargs='?', default=30, type=int, help="Days, integer, default: 30")

    def do_job(self):
        """
        SELECT sum(t.end_time - t.start_time)
        FOM task t
        GROUP BY day(t.start_time)
        WHERE start_time > GetDate() - @days
        :return:
        """
        session = DBSession()
        daywork = func.sum(func.julianday(Task.end_time) - func.julianday(Task.start_time)) * 86400
        day = func.date(Task.start_time)
        query = session.query(day, daywork) \
            .group_by(day) \
            .filter(func.date(Task.start_time) > func.date('now', '-%s day' % self.args.days)) \
            .filter(Task.end_time != None) \
            .order_by(Task.start_time)

        print()

        table = PrettyTable(['Day', 'Work Time', 'Graph'])
        table.align["Graph"] = "l"
        total_hours = timedelta(0)
        last_day = None
        for row in query:
            day = datetime.strptime(row[0], '%Y-%m-%d').date()
            if last_day:
                diff = (day - last_day)
                for i in range(diff.days - 1):
                    table.add_row([last_day + timedelta(i + 1), 0, ''])

            worktime = timedelta(seconds=round(row[1]))
            total_hours += worktime
            table.add_row([day, worktime, '#' * int(round((row[1] * 60 / 86400)))])
            last_day = day

        print(table)
        print('Total Work time: %s\n' % total_hours)
