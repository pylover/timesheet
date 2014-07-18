
__author__ = 'vahid'

from timesheet.commands import Command
from timesheet.models import Subject, DBSession
from timesheet.commands.completers import subject_completer


class RenameCommand(Command):
    name = 'rename'
    description = 'Renames a subject'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('subject', help="Subject to do something about that.").completer = subject_completer
        cls.parser.add_argument('new_name', help="Subject's new name").completer = subject_completer

    def do_job(self):
        if self.args.subject:
            subject = Subject.query.filter(Subject.title == self.args.subject).first()
            if not subject:
                print 'Subject can not found: %s' % self.args.subject
            else:
                subject.title = self.args.new_name
                DBSession.commit()
        else:
            print "Please specify a subject to rename"


