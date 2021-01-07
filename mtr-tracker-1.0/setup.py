#!/usr/bin/env python3

import os
import sys
from setuptools import setup

if sys.version_info < (3,6):
    print('mtr-tracker requires Python 3.6 or higher')
    sys.exit(1)

_VERSION = '1.0'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mtr-tracker",
    version=_VERSION,
    author="Thiago Oliveira",
    author_email="thredhat@gmail.com",
    description="Traceroute ISP information and location with API to http://ip-api.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MuGrU/mtr-tracker",
    download_url='https://github.com/MuGrU/mtr-tracker/mtr-tracker-%s.tar.gz' % _VERSION,
    license='GPLv3',
    platforms='Linux',
    scripts=[
        'bin/mtr-tracker',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System Kernels :: Linux",
    ],
)
