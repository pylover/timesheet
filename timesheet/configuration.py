__author__ = 'vahid'

from pymlconf import ConfigManager
from os import path, mkdir
from appdirs import user_data_dir, user_config_dir

user_data_file = path.abspath(path.join(user_data_dir(), 'timesheet', 'timesheet.sqlite'))
user_config_file = path.abspath(path.join(user_config_dir(), 'timesheetrc'))

__builtin_config__ = """
db:
  uri: sqlite:///%(data_file)s
  echo: false

datetime_format: %(time_format)s

""" % dict(data_file=user_data_file,
           time_format='"%Y/%m/%d %H:%M"')


def create_config_manager():

    data_dir = path.dirname(user_data_file)
    if not path.exists(data_dir):
        mkdir(data_dir)

    return ConfigManager(__builtin_config__, files=user_config_file)
