from _ast import Import

__author__ = 'vahid'

from timesheet.commands import Command
from timesheet import config
import sys
import csv
from datetime import datetime
from timesheet.models import Subject


class ImportCommand(Command):
    name = 'import'
    description = 'Import csv file with columns: subject, task, start, end'

    def __init__(self, *args, **kw):
        super(ImportCommand, self).__init__(*args, **kw)
        self.subjects = {}

    def add_arguments(self):
        self.parser.add_argument('input', nargs='?', help="Input filename. if omitted, the standard input will be used")

    def process_row(self, row):
        subject_name, task_name, start_time, end_time = row
        start_time = datetime.strptime(start_time, config.datetime_format)
        end_time = datetime.strptime(end_time, config.datetime_format)

        if not subject_name in self.subjects:
            self.subjects[subject_name] = Subject.ensure(subject_name)


        print subject_name, task_name, start_time, end_time

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


