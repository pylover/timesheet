__author__ = 'vahid'


from timesheet.commands import Command


class HelpCommand(Command):
    name = 'help'
    description = 'Prints help for given command'

    def add_arguments(self):
        self.parser.add_argument('command', help="Command to print help about that")

    def do_job(self):
        command_class = Command.get_command(self.args.command)
        command_class(args=[]).help()
