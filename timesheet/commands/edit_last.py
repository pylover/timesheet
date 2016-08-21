# -*- coding: utf-8 -*-
from timesheet.commands import Command
from timesheet.models import Task, DBSession
import argparse
__author__ = 'vahid'


class EditLastCommand(Command):
    name = 'edit-last'
    description = 'Edit last task'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('task', nargs=argparse.REMAINDER, default=[], help="The task name")

    def do_job(self):
        task = Task.get_last_task()
        if task:
            task.title = ' '.join(self.args.task)
            DBSession.commit()
        else:
            print('Last task not found')
