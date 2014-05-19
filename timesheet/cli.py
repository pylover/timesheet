__author__ = 'vahid'

import argparse
import argcomplete
from timesheet.configuration import user_config_file
from timesheet.commands import Command
#from argcomplete.completers import EnvironCompleter

commands = ''.join(['\n %-20s%s' % (c.name, c.description) for c in Command.get_available_commands()])

parser = argparse.ArgumentParser(description='Simple timesheet system, using python',
                                 epilog="Available commands:%s" % commands,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)

parser.add_argument('command', help='Command')

parser.add_argument('-c', '--config-file',
                    dest='config_files',
                    action='append',
                    default=[user_config_file],
                    help='YAML configuration file, this option can be used multiple times \
                    , default: %s' % user_config_file)

argcomplete.autocomplete(parser)

REMINDER = []


def parse_ars():
    global REMINDER
    args, REMINDER = parser.parse_known_args()
    return args


def dispatch_command(command):
    command_class = Command.get_command(command)
    cmd = command_class(REMINDER)
    cmd.do_job()