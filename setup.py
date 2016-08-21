# -*- coding: utf-8 -*-
import os
import re
from setuptools import find_packages
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# reading cherryblog.py version without importing any modules from that package
with open(os.path.join(os.path.dirname(__file__), 'timesheet', '__init__.py')) as v_file:
    package_version = re.compile(r".*__version__ = '(.*?)'", re.S).match(v_file.read()).group(1)

dependencies = [
    'sqlalchemy',
    'pymlconf>=0.3.10',
    'appdirs>=1.3.0',
    'argcomplete',
    'PrettyTable'
]


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="timesheet",
    version=package_version,
    author="Vahid Mardani",
    author_email="vahid.mardani@gmail.com",
    url="http://github.com/pylover/timesheet",
    description="Simple timesheet tracking system",
    packages=find_packages(exclude=['ez_setup']),
    platforms=["any"],
    long_description=read('README.rst'),
    install_requires=dependencies,
    dependency_links=[
        'git+https://github.com/pylover/elixir.git#egg=elixir-0.8.1'
    ],
    entry_points={
        'console_scripts': [
            'timesheet = timesheet:entrypoint'
        ]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: Freeware",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

)
