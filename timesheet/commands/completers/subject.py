__author__ = 'vahid'


from timesheet.models import Subject


# noinspection PyUnusedLocal
def subject_completer(prefix, **kwargs):
    return [c for c in Subject.all_titles() if c.startswith(prefix)]
