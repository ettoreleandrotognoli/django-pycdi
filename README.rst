DJango + PyCDI
==============

.. image:: https://travis-ci.org/ettoreleandrotognoli/django-pycdi.svg?branch=master
    :target: https://travis-ci.org/ettoreleandrotognoli/django-pycdi

.. image:: https://codecov.io/gh/ettoreleandrotognoli/django-pycdi/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/ettoreleandrotognoli/django-pycdi

.. image:: https://badge.fury.io/py/django-pycdi.svg
    :target: https://badge.fury.io/py/django-pycdi

.. image:: https://img.shields.io/pypi/dm/django-pycdi.svg
    :target: https://pypi.python.org/pypi/django-pycdi#downloads

A middleware to integrate PyCDI_ with DJango.


Install
-------

Install pypi version

.. code-block :: shell

    pip install django_pycdi

Install lastest version

.. code-block :: shell

    pip install git+https://github.com/ettoreleandrotognoli/django-pycdi.git
    

Usage
-----

Add middleware to settings.py

.. code-block :: python
    
    MIDDLEWARE += 'django_pycdi.middlewares.CDIMiddleware'



Add inject decorator to your views

Python 2

.. code-block :: python

    from random import random
    from pycdi import Inject, Producer
    from pycdi.utils import Singleton
    
    
    @Singleton()
    class MySingleton():
        pass
    
    @Producer(float)
    def get_a_float():
        return random()

    @Inject(singleton=MySingleton,number=float)
    def view(request,singleton,number):
        return HttpResponse('...')


Python 3

.. code-block :: python

    from random import random
    from pycdi import Inject, Producer
    from pycdi.utils import Singleton
    
    @Singleton()
    class MySingleton():
        pass
        
    @Producer()
    def get_a_float() -> float:
        return random()
    
    @Inject()
    def view(request,singleton:MySingleton,number:float):
        return HttpResponse('...')

See more in the PyCDI_ page.

.. _PyCDI: https://github.com/ettoreleandrotognoli/python-cdi

