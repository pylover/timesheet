
__author__ = 'vahid'

from timesheet.commands import Command
from timesheet.models import Subject


class SubjectsCommand(Command):
    name = 'subjects'
    description = 'Print all subjects'

    def do_job(self):
        print '\n'.join(Subject.all_titles())
