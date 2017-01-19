# -*- coding: utf-8 -*-
import sys
import csv
from datetime import datetime

from timesheet.commands import Command
from timesheet.models import Task, Subject
from timesheet.commands.completers import subject_completer


class ExportCommand(Command):
    name = 'export'
    description = 'Export the database into csv file with columns: subject, task, start, end'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('output', nargs='?', help="Output filename. if omitted, \
        the standard output will be used")
        cls.parser.add_argument('-s', '--subject',
                                action='append',
                                default=[],
                                help="Subject to filter the result ")\
            .completer = subject_completer
        cls.parser.add_argument('--from', dest='from_', metavar="FROM", help='example: 2016-12-21')
        cls.parser.add_argument('--to', help='example: 2016-12-21')
        cls.parser.add_argument('--time-format', default='%Y-%m-%d',
                                help="Date time format to parse --from/--to values, default: %%Y-%%m-%%d")

    def parse_datetime(self, string_value):
        return datetime.strptime(string_value, self.args.time_format)

    def do_job(self):

        if self.args.output:
            csv_file = open(self.args.output, 'w')
        else:
            csv_file = sys.stdout

        try:
            query = Task.query.join(Task.subject).order_by(Subject.entry_time, Task.start_time)
            if self.args.subject:
                query = query.filter(Subject.title.in_(self.args.subject))

            elif self.args.from_:
                query = query.filter(Task.start_time >= self.parse_datetime(self.args.from_))

            elif self.args.to:
                query = query.filter(Task.start_time <= self.parse_datetime(self.args.to))

            writer = csv.writer(csv_file)
            for task in query:
                writer.writerow([task.subject.title, task.title, task.start_time_string, task.end_time_string, task.duration_formatted])
        finally:
            if csv_file and csv_file != sys.stdout:
                csv_file.close()
