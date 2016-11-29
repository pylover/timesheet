
from timesheet.models import Subject, Task


def subject_completer(prefix, **kwargs):
    try:
        return [c for c in Subject.all_titles() if c.startswith(prefix)]
    except Exception as ex:
        return [str(ex)]


def task_completer(prefix, **kwargs):
    try:
        return [c for c in Task.all_titles() if c.startswith(prefix)]
    except Exception as ex:
        return [str(ex)]
