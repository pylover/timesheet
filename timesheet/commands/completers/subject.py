# -*- coding: utf-8 -*-
from timesheet.models import Subject
__author__ = 'vahid'


# noinspection PyUnusedLocal
def subject_completer(prefix, **kwargs):
    try:
        return [c for c in Subject.all_titles() if c.startswith(prefix)]
    except Exception as ex:
        return [str(ex)]
