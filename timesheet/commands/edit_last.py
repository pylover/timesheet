
from datetime import datetime

from timesheet.models import Task, DBSession
from timesheet.commands import Command
from timesheet import config


class EditLastCommand(Command):
    name = 'edit-last'
    description = 'Edit last task'
    time_format = '%Y-%m-%d %H:%M:%S.%f'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('--title', help="The task's title")
        cls.parser.add_argument('--end-time', help="The end time of the task")
        cls.parser.add_argument('--start-time', help="The start time of the task")
        cls.parser.add_argument('--time-format', default=cls.time_format,
                                help="Date time format to parse --from/--to values, default: " +
                                     cls.time_format.replace('%', '%%'))

    def parse_datetime(self, string_value):
        return datetime.strptime(string_value, self.time_format)

    def do_job(self):
        task = Task.get_last_task()
        if task:
            if self.args.title:
                task.title = self.args.title

            if self.args.end_time:
                task.end_time = self.parse_datetime(self.args.end_time)

            if self.args.start_time:
                task.start_time = self.parse_datetime(self.args.start_time)

            DBSession.commit()
        else:
            print('Last task not found')
