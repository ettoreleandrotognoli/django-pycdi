# -*- encoding: utf-8 -*-
__author__ = 'ettore'

import os
from setuptools import setup, find_packages

from django_pycdi import __version__


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


requirements = []
str_version = '.'.join(map(str, __version__))

setup(
    name='django-pycdi',
    version=str_version,
    description='DJango with Code Dependency Injection using PyCDI',
    long_description=read('README.rst'),
    url='https://github.com/ettoreleandrotognoli/django-pycdi',
    download_url='https://github.com/ettoreleandrotognoli/django-pycdi/tree/%s/' % str_version,
    license='BSD',
    author=u'Éttore Leandro Tognoli',
    author_email='ettore.leandro.tognoli@gmail.com',
    packages=find_packages(exclude=['tests', 'demo2', 'demo3']),
    include_package_data=True,
    keywords=['django', 'pycdi', 'cdi', 'di', 'code dependency injection', 'dependency injection'],
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 2 - Pre-Alpha',
        'Framework :: DJango',
        'License :: OSI Approved :: BSD License',
    ],
    install_requires=[
        'pycdi>=0.0.2'
    ],
    # tests_require=[],
)
