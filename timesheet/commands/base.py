
class Command(object):
    """
    Abstract command class
    """
    name = ''
    description = ''
    parser = None

    def __init__(self, args):
        self.args = args

    @classmethod
    def create_parser(cls, subparsers):
        cls.parser = subparsers.add_parser(cls.name, help=cls.description)
        cls.parser.set_defaults(command_class=cls)
        cls.add_arguments()
        return cls.parser

    @classmethod
    def add_arguments(cls):
        pass

    @classmethod
    def help(cls):
        cls.parser.print_help()

    def do_job(self):
        raise NotImplementedError()


def __get_available_commands(command_class):
    commands = command_class.__subclasses__()
    for c in list(commands):
        commands.extend(__get_available_commands(c))
    return commands


def get_available_commands():
    return __get_available_commands(Command)


def get_available_command_names():
    return [c.name for c in get_available_commands()]


def get_command(command_name):
    for c in get_available_commands():
        if c.name == command_name:
            return c
    raise ValueError('Invalid command name: %s' % command_name)
