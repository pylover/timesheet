__author__ = 'vahid'

import argparse


class Command(object):

    def __init__(self, args=None):
        self.parser = self._create_parser()
        self.add_arguments()
        self.args = self.parser.parse_args(args=args)

    def _create_parser(self, **kwargs):
        kwargs['description'] = self.description
        kwargs['prog'] = '%s %s' % ('timesheet', self.name)
        kwargs['add_help'] = False
        return argparse.ArgumentParser(**kwargs)

    def add_arguments(self):
        pass

    def help(self):
        self.parser.print_help()

    def do_job(self):
        raise NotImplementedError()

    @classmethod
    def get_available_commands(cls):
        commands = cls.__subclasses__()
        for c in list(commands):
            commands.extend(c.get_available_commands())
        return commands

    @classmethod
    def get_command(cls, command_name):
        for c in cls.get_available_commands():
            if c.name == command_name:
                return c
        raise ValueError('Invalid command name: %s' % command_name)


from .start import StartCommand
from .help import HelpCommand

__all__ = ['Command', 'StartCommand', 'HelpCommand']