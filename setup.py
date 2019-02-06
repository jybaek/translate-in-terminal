#!/usr/bin/env python

try: # for pip >= 10
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
    from pip.download import PipSession

################################################################################
# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements("requirements.txt", session=PipSession())
from setuptools import setup, find_packages
from translatebot import __version__ as version

# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = [str(ir.req) for ir in install_reqs]

# Package meta-data.
NAME = 'translatebot'
DESCRIPTION = 'This translator uses the google translate api. ' \
              'Do not open your browser for translation anymore. ' \
              'We do not like touching the mouse or annoying you..'
URL = 'https://github.com/jybaek/translate-in-terminal'
EMAIL = 'caleybaek@gmail.com'
AUTHOR = 'Caley Baek'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = version

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    download_url='',
    install_requires=reqs,
    packages=find_packages(include=['translatebot*', 'tests', ]),
    keywords=['translate', 'google'],
    python_requires='>=3',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    entry_points={
              'console_scripts': [
                  'translatebot=translatebot.translatebot:main',
              ],
          },
)
