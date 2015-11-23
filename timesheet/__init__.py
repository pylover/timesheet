__author__ = 'vahid'
__version__ = '0.7.1'

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

    # Dispatch and execute the command
    args.command_class(args).do_job()

    sys.exit(0)