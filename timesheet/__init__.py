__author__ = 'vahid'
__version__ = '0.1dev'

import sys
from timesheet.configuration import create_config_manager

config = create_config_manager()


def entrypoint():
    global config

    # initializing models
    from timesheet import models
    models.init()

    # Preparing cli arguments
    from timesheet import cli
    args = cli.parse_ars()

    # Switch on commands
    cli.dispatch_command(args)

    sys.exit(0)