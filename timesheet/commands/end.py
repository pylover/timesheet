# -*- coding: utf-8 -*-
from timesheet.commands import Command
from timesheet.models import Task, DBSession
__author__ = 'vahid'


class EndCommand(Command):
    name = 'end'
    description = 'Ends a task'

    def do_job(self):
        active_task = Task.get_active_task()
        if not active_task:
            print("You don't have any active task")
            return

        active_task.end()
        DBSession.commit()
        print('Task ended: %s' % active_task)
