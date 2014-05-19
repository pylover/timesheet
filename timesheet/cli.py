__author__ = 'vahid'

import argparse
import argcomplete
from timesheet.configuration import user_config_file
from timesheet.commands import get_available_commands


# commands_help_list = ''.join(['\n %-20s%s' % (c.name, c.description) for c in commands])
# command_names = [c.name for c in commands]

def create_parser():

    parser = argparse.ArgumentParser(description='Simple timesheet system, using python')

    parser.add_argument('-c', '--config-file',
                        dest='config_files',
                        action='append',
                        default=[user_config_file],
                        help='YAML configuration file, this option can be used multiple times \
                        , default: %s' % user_config_file)

    subparsers = parser.add_subparsers(title='subcommands',
                                       description='valid subcommands')

    for cmd in get_available_commands():
        cmd.create_parser(subparsers)

    argcomplete.autocomplete(parser)

    return parser


REMINDER = []


def parse_ars():
    parser = create_parser()
    global REMINDER
    args, REMINDER = parser.parse_known_args()
    return args


def dispatch_command(args):
    command_class = args.command_class
    cmd = command_class(args)
    cmd.do_job()