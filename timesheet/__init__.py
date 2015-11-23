# -*- coding: utf-8 -*-
import sys
from timesheet.configuration import init_config, config
__author__ = 'vahid'
__version__ = '0.8.1'


def entrypoint():
    global config

    # Preparing cli arguments
    from timesheet import cli
    args = cli.parse_ars()

    config = init_config(args.config_file)

    # initializing models
    from timesheet import models
    models.init()

    # Dispatch and execute the command
    args.command_class(args).do_job()

    sys.exit(0)
