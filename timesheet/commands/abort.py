# -*- coding: utf-8 -*-
from timesheet.commands import Command
from timesheet.models import Task, DBSession
__author__ = 'vahid'


class AbortCommand(Command):
    name = 'abort'
    description = 'Aborts currently active task'

    def do_job(self):
        active_task = Task.get_active_task()
        if active_task:
            print('Aborting active task: %s' % active_task)
            DBSession.delete(active_task)
            DBSession.commit()
        else:
            print("You don't have any active task")
