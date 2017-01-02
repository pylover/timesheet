# -*- coding: utf-8 -*-
from timesheet.commands import Command
from timesheet.models import Subject, Task
from timesheet.commands.completers import subject_completer
from prettytable import PrettyTable
from datetime import timedelta, date, datetime
__author__ = 'vahid'


class FullReportCommand(Command):
    name = 'report'
    description = 'Print report about an subject or all subjects'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('subject', nargs='?', help="Subject to do something about that.")\
            .completer = subject_completer
        cls.parser.add_argument('--today', action='store_true', help="Only prints today's tasks.")
        cls.parser.add_argument('--from', dest='from_', help='example: 2016.12.21')
        cls.parser.add_argument('--to', help='example: 2016.12.21')
        cls.parser.add_argument('--time-format', default='%Y.%m.%d', help="Date time format to parse --from/--to values"
                                                                          ", default: %Y.%m.%d")

    def report_subject(self, subject):

        print('\n%s' % subject.title)

        table = PrettyTable(['Task Name', 'Duration', 'From', 'To'])
        table.align["Task Name"] = "l"
        table.align["Duration"] = "c"
        table.padding_width = 1  # default

        q = Task.query.filter(Task.subject == subject)
        if self.args.today:
            q = q.filter(Task.start_time > date.today())

        elif self.args.from_:
            q = q.filter(Task.start_time >= self.parse_datetime(self.args.from_))

        elif self.args.to:
            q = q.filter(Task.start_time <= self.parse_datetime(self.args.to))

        q = q.order_by(Task.start_time)

        total_duration = timedelta()
        for task in q:
            total_duration += task.duration
            table.add_row(['' if not task.title else task.title,
                           task.duration_formatted,
                           task.start_time_string,
                           task.end_time_string])

        print(table)
        ts = total_duration.total_seconds()
        h = ts / 3600
        m = (ts % 3600) / 60
        print('Total: %.2d:%.2d\n' % (h, m))

    def parse_datetime(self, string_value):
        return datetime.strptime(string_value, self.args.time_format)

    def do_job(self):
        if self.args.subject:
            subject = Subject.query.filter(Subject.title == self.args.subject).first()
            if not subject:
                print('Subject can not found: %s' % self.args.subject)
            else:
                self.report_subject(subject)
        else:
            for subject in Subject.query.order_by(Subject.entry_time):
                self.report_subject(subject)
