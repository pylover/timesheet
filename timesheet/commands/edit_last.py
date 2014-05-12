__author__ = 'vahid'

from timesheet.commands import Command
from timesheet.models import Subject, Task, DBSession


class EditLastCommand(Command):
    name = 'edit-last'
    description = 'Edit last task'

    def add_arguments(self):
        self.parser.add_argument('task', help="The task name")

    def do_job(self):
        task = Task.get_last_task()
        if task:
            task.title = self.args.task
            DBSession.commit()
        else:
            print 'Last task not found'


