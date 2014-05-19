__author__ = 'vahid'
__version__ = '0.1dev'

import sys
from timesheet.configuration import create_config_manager

config = create_config_manager()


def entrypoint():
    global config

    # Preparing cli arguments
    from timesheet import cli
    args = cli.parse_ars()

    # Preparing config
    config.load_files(args.config_files)

    # initializing models
    from timesheet import models
    models.init()

    # Switch on commands
    cli.dispatch_command(args)

    sys.exit(0)