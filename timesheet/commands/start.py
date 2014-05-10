__author__ = 'vahid'

from timesheet.commands import Command
from timesheet.models import Subject, Task, DBSession


class StartCommand(Command):
    name = 'start'
    description = 'Starts a task'

    def add_arguments(self):
        self.parser.add_argument('subject', help="Subject to do something about that.")
        self.parser.add_argument('task', nargs='?', help="The task name")

    def do_job(self):
        active_task = Task.get_active_task()
        if active_task:
            print 'You have an active task: %s' % active_task
            print 'Please end this task before starting another one'
            return

        subject = Subject.ensure(self.args.subject)
        task = Task(title=self.args.task)
        subject.tasks.append(task)

        DBSession.commit()
        print 'Started task: %s' % task


