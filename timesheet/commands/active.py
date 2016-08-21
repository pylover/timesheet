# -*- coding: utf-8 -*-
from timesheet.commands import Command
from timesheet.models import Task
__author__ = 'vahid'


class ActiveCommand(Command):
    name = 'active'
    description = 'Prints active task'

    def do_job(self):
        active_task = Task.get_active_task()
        if active_task:
            print('Active task: %s' % active_task)
        else:
            print("You don't have any active task")
