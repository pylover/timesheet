# -*- coding: utf-8 -*-
from timesheet.commands.completers import subject_completer
from timesheet.commands import Command
from timesheet.models import Subject, DBSession
__author__ = 'vahid'


class DeleteCommand(Command):
    name = 'delete'
    description = 'Deletes a subject '

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('subject', nargs='?', help="Subject to delete.")\
            .completer = subject_completer

    def do_job(self):
        subject = Subject.query.filter(Subject.title == self.args.subject).first()
        if not subject:
            print('Subject can not found: %s' % self.args.subject)
        else:
            DBSession.delete(subject)
            DBSession.commit()

        print("Subject `%s` was deleted successfully" % self.args.subject)
