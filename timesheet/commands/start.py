__author__ = 'vahid'

from timesheet.commands import Command


class StartCommand(Command):
    name = 'start'
    description = 'Starts a task'

    def add_arguments(self):
        self.parser.add_argument('subject', help="Subject to do something about that.")
        self.parser.add_argument('task', nargs='?', help="The task name")

    def do_job(self):
        print self.args