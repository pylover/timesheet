# -*- coding: utf-8 -*-
from timesheet.commands import Command
from timesheet.models import Subject, DBSession
from timesheet.commands.completers import subject_completer
__author__ = 'vahid'


class RenameCommand(Command):
    name = 'rename'
    description = 'Renames a subject'

    @classmethod
    def add_arguments(cls):
        cls.parser.add_argument('subject', help="Subject to do something about that.").completer = subject_completer
        cls.parser.add_argument('new_name', help="Subject's new name").completer = subject_completer

    def do_job(self):
        if not self.args.subject:
            print("Please specify a subject to rename")

        subject = Subject.query.filter(Subject.title == self.args.subject).first()
        if not subject:
            print('Subject can not found: %s' % self.args.subject)
            return

        new_subject = Subject.query.filter(Subject.title == self.args.new_name).first()
        if new_subject:
            print("There is already a subject with name: %s" % self.args.new_name)
            answer = raw_input("Do you want to merge these subjects? [Y/n]: ")
            if not answer or answer.lower() == 'y':
                for task in subject.tasks:
                    task.subject = new_subject
                DBSession.flush()
                DBSession.delete(subject)
                DBSession.commit()
            else:
                print('Operation aborted by user.')

        else:
            subject.title = self.args.new_name
            DBSession.commit()
