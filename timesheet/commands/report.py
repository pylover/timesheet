__author__ = 'vahid'

from timesheet.commands import Command
from timesheet.models import Subject, Task, DBSession
from timesheet import config

class ReportCommand(Command):
    name = 'report'
    description = 'Print report about an subject or all subjects'

    def add_arguments(self):
        self.parser.add_argument('subject', nargs='?', help="Subject to do something about that.")

    @staticmethod
    def report_subject(subject):
        print '\n'
        print '#' * 65
        print '%s' % subject.title, '\n'

        print '|%-20s|%-8s|%-16s|%-16s|' % ('Task Name', 'Hours', 'From', 'To')
        print '+%-20s+%8s+%16s+%16s+' % ('-' * 20, '-' * 8, '-' * 16, '-' * 16)
        total_hours = 0
        for task in subject.tasks:
            total_hours += task.hours
            print '|%-20s|%8.2f|%-16s|%-16s|' % (
                '' if not task.title else task.title[:20],
                task.hours,
                task.start_time.strftime(config.datetime_format),
                '' if not task.end_time else task.end_time.strftime(config.datetime_format)
            )

        print '+%-20s+%8s+%16s+%16s+' % ('-' * 20, '-' * 8, '-' * 16, '-' * 16)
        print '|%-20s|%8.2f|' % ('Total', total_hours)
        print '\n'

    def do_job(self):
        if self.args.subject:
            subject = Subject.query.filter(Subject.title == self.args.subject).first()
            if not subject:
                print 'Subject can not found: %s' % self.args.subject
            else:
                self.report_subject(subject)
        else:
            for subject in Subject.query.order_by(Subject.entry_time):
                self.report_subject(subject)


