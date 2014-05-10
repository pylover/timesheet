__author__ = 'vahid'

from timesheet.commands import Command
import sys
import csv
from timesheet.models import Subject


class ImportCommand(Command):
    name = 'import'
    description = 'Import csv file with columns: subject, task, start, end'

    def add_arguments(self):
        self.parser.add_argument('input', nargs='?', help="Input filename. if omitted, the standard input will be used")

    def do_job(self):

        if self.args.input:
            csv_file = open(self.args.input)
        else:
            csv_file = sys.stdin

        try:
            reader = csv.reader(csv_file)
            for row in reader:
                print ', '.join(row)
        finally:
            if csv_file and csv_file != sys.stdin:
                csv_file.close()


