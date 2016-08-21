# -*- coding: utf-8 -*-
from timesheet.commands import Command, get_command, get_available_command_names
from argcomplete.completers import ChoicesCompleter
__author__ = 'vahid'


class HelpCommand(Command):
    name = 'help'
    description = 'Prints help for given command'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('command', nargs='?', help="Command to print help about that").completer = \
            ChoicesCompleter(get_available_command_names())

    def do_job(self):
        if self.args.command:
            command_class = get_command(self.args.command)
            command_class.help()
        else:
            from timesheet.cli import parser
            parser.print_help()
