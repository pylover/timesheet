__author__ = 'vahid'


from timesheet.commands import Command, get_command


class HelpCommand(Command):
    name = 'help'
    description = 'Prints help for given command'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('command', help="Command to print help about that")

    def do_job(self):
        command_class = get_command(self.args.command)
        command_class.help()
