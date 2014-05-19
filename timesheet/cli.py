__author__ = 'vahid'

import argparse
import argcomplete
from timesheet.commands import get_available_commands


def create_parser():

    parser = argparse.ArgumentParser(description='Simple timesheet system, using python')
    subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands')

    for cmd in get_available_commands():
        cmd.create_parser(subparsers)

    argcomplete.autocomplete(parser)
    return parser


def parse_ars():
    parser = create_parser()
    args, _reminder = parser.parse_known_args()
    return args


def dispatch_command(args):
    command_class = args.command_class
    cmd = command_class(args)
    cmd.do_job()