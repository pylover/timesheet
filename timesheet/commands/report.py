__author__ = 'vahid'

from timesheet.commands import Command
from timesheet.models import Subject, Task, DBSession


class ReportCommand(Command):
    name = 'report'
    description = 'Print report about an subject or all subjects'

    def add_arguments(self):
        self.parser.add_argument('subject', nargs='?',help="Subject to do something about that.")

    def do_job(self):
        pass


