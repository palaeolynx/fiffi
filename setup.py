"""
    Setup fiffi package.
"""

import ast
import re

from setuptools import setup, find_packages


def get_version():
    """Gets the current version"""
    _version_re = re.compile(r'__VERSION__\s+=\s+(.*)')
    with open('fiffi/__init__.py', 'rb') as init_file:
        version = str(ast.literal_eval(_version_re.search(
            init_file.read().decode('utf-8')).group(1)))
    return version


setup(
    name='fiffi',
    version=get_version(),
    license='LGPL',

    description='Test',

    url='https://github.com/palaeolynx/fiffi',

    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        'aptly'
    ],

    keywords=[
        'tool',
        'proxy'
        'chaib'
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'Topic :: Utilities'
    ],
)
