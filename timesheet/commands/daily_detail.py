# -*- coding: utf-8 -*-
from timesheet.commands import Command
from timesheet.models import DBSession, Task, Subject
from prettytable import PrettyTable
from datetime import timedelta, datetime
from sqlalchemy import func

__author__ = 'gmc'


class DailyDetailCommand(Command):
    name = 'daily-detail'
    description = 'Print detailed daily report'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('days', nargs='?', default=30, type=int, help="Days, integer, default: 30")

    def do_job(self):
        """
        SELECT *, coalesce(end_time,now)-start_time
        FROM task t, subject s
        WHERE t.subject_id=s.id AND start_time > GetDate() - @days
        ORDER BY start_time
        :return:
        """
        session = DBSession()
        now = datetime.now()
        time_worked = (func.julianday(func.coalesce(Task.end_time,now)) - func.julianday(Task.start_time)) * 86400

        query = session.query(Task.start_time,
                              func.coalesce(Task.end_time, now),
                              time_worked,
                              Subject.title,
                              Task.title) \
            .filter(Subject.id == Task.subject_id) \
            .filter(func.date(Task.start_time) > func.date('now', '-%s day' % self.args.days)) \
            .order_by(Task.start_time)

        print()

        table = PrettyTable(['Start', 'End', 'Time', 'Subject', 'Title'])
        table.align["Title"] = "l"

        total_time = 0
        day_total = 0
        last_date = None

        for row in query:
            if last_date == None:
                last_date = row[0].date()

            if row[0].date() != last_date:
                table.add_row([
                    '', '', timedelta(seconds=round(day_total)), '', ''
                ])
                last_date = row[0].date()
                day_total = 0

            day_total += row[2]
            total_time += row[2]

            table.add_row([
                row[0],
                row[1],
                timedelta(seconds=round(row[2])),
                row[3],
                row[4],
            ])

        if day_total > 0:
            table.add_row([
                '', '', timedelta(seconds=round(day_total)), '', ''
            ])

        print(table)
        print('Total Work time: %s\n' % timedelta(seconds=total_time))
