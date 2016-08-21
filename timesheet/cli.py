# -*- coding: utf-8 -*-
import argparse
import argcomplete
from timesheet.commands import get_available_commands
__author__ = 'vahid'


parser = argparse.ArgumentParser(description='Simple timesheet system.')
subparsers = parser.add_subparsers(title='Commands', description='')

for cmd in get_available_commands():
    cmd.create_parser(subparsers)

argcomplete.autocomplete(parser)


def parse_ars():
    # args, _reminder = parser.parse_known_args()
    args = parser.parse_args()
    return args
