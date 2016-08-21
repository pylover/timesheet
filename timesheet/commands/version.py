# -*- coding: utf-8 -*-
import timesheet
from timesheet.commands import Command
__author__ = 'vahid'


class VersionCommand(Command):
    name = 'version'
    description = 'Prints the version'

    def do_job(self):
        print(timesheet.__version__)
