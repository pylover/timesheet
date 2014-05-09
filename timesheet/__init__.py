__author__ = 'vahid'
__version__ = '0.1dev'

import sys
from timesheet import cli
from timesheet.configuration import create_config_manager
from timesheet import models
from timesheet.commands import Command

config = create_config_manager()


def entrypoint():
    global config

    # Preparing cli arguments
    args, remainder = cli.parser.parse_known_args()

    # Preparing config
    config.load_files(args.config_files)

    # initializing models
    models.init()

    # Switch on commands
    command_class = Command.get_command(args.command)
    cmd = command_class(remainder)
    cmd.do_job()


    sys.exit(0)