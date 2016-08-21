
timesheet
=========

install
^^^^^^^

    $ pip install timesheet
        
        
usage
^^^^^

::

    $ timesheet help
    usage: timesheet [-h]
                     {help,start,end,active,report,subjects,import,export,edit-last,abort,rename,daily-report,daily-detail,delete,version}
                     ...

    Simple timesheet system.

    optional arguments:
      -h, --help            show this help message and exit

    Commands:

      {help,start,end,active,report,subjects,import,export,edit-last,abort,rename,daily-report,daily-detail,delete,version}
        help                Prints help for given command
        start               Starts a task
        end                 Ends a task
        active              Prints active task
        report              Print report about an subject or all subjects
        subjects            Print all subjects
        import              Import csv file with columns: subject, task, start,
                            end
        export              Export the database into csv file with columns:
                            subject, task, start, end
        edit-last           Edit last task
        abort               Aborts currently active task
        rename              Renames a subject
        daily-report        Print daily report
        daily-detail        Print detailed daily report
        delete              Deletes a subject
        version             Prints the version

Help on Help
^^^^^^^^^^^^

::

    $ timesheet help -h
    usage: timesheet help [-h] [command]

    positional arguments:
      command     Command to print help about that

    optional arguments:
      -h, --help  show this help message and exit


Bash Auto-Completion
^^^^^^^^^^^^^^^^^^^^

::

    $ echo "eval \"\$(register-python-argcomplete timesheet)\"" >> ~/.bashrc
    $ source ~/.bashrc


Change Log
^^^^^^^^^^

* 0.9.2
    * Supporting python3

* 0.8.4
    * Adding daily-report command by `sonologic <https://github.com/sonologic>`_
    * Reformatting README.md to README.rst for pypi
    * Updating README.rst
