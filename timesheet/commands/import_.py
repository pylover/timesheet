# -*- coding: utf-8 -*-
import sys
import csv
from timesheet.commands import Command
from timesheet import config
from timesheet.models import Subject, DBSession, Task
from datetime import datetime
__author__ = 'vahid'


class ImportCommand(Command):
    name = 'import'
    description = 'Import csv file with columns: subject, task, start, end'

    def __init__(self, *args, **kw):
        super(ImportCommand, self).__init__(*args, **kw)
        self.subjects = {}

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('input', nargs='?', help="Input filename. if omitted, the standard input will be used")

    def process_row(self, row):
        subject_name, task_name, start_time, end_time = row
        start_time = datetime.strptime(start_time, config.datetime_format)
        end_time = datetime.strptime(end_time, config.datetime_format)

        if subject_name not in self.subjects:
            self.subjects[subject_name] = Subject.ensure(subject_name)
            DBSession.commit()

        task = Task(title=task_name, start_time=start_time, end_time=end_time)
        self.subjects[subject_name].tasks.append(task)
        print('Adding %s' % task)
        DBSession.commit()

    def do_job(self):

        if self.args.input:
            csv_file = open(self.args.input)
        else:
            csv_file = sys.stdin

        try:
            reader = csv.reader(csv_file)
            for row in reader:
                self.process_row(row)
        finally:
            if csv_file and csv_file != sys.stdin:
                csv_file.close()
