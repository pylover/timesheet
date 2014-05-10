__author__ = 'vahid'
__version__ = '0.1dev'

import sys
from timesheet.configuration import create_config_manager

config = create_config_manager()


def entrypoint():
    global config

    # Preparing cli arguments
    from timesheet import cli
    args, remainder = cli.parser.parse_known_args()

    # Preparing config
    config.load_files(args.config_files)

    # initializing models
    from timesheet import models
    models.init()

    # Switch on commands
    from timesheet.commands import Command
    command_class = Command.get_command(args.command)
    cmd = command_class(remainder)
    cmd.do_job()


    sys.exit(0)