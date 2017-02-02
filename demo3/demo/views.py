from random import random

from django.http import HttpRequest
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import View
from pycdi import Inject, Producer
from pycdi.core import CDIContainer
from pycdi.utils import Singleton


@Singleton()
class MySingleton(object):
    pass


@Producer()
def produce_random() -> float:
    return random()


def without_injection(request, *args, **kwargs):
    return render(request, 'debug.html', locals())


@Inject()
def with_injection(request, data, url: str, singleton: MySingleton, random_number: float):
    return render(request, 'debug.html', locals())


@Inject()
def with_request_injection(request: HttpRequest, singleton: MySingleton, random_number: float):
    return render(request, 'debug.html', locals())


@Inject()
def container_inject(request, container: CDIContainer, number: float):
    singleton = container.produce(MySingleton)
    return render(request, 'debug.html', locals())


@method_decorator(Inject(), name='dispatch')
class GenericView(View):
    def get(self, request, container: CDIContainer, number: float):
        other_number = container.produce(float)
        singleton = container.produce(MySingleton)
        return render(request, 'debug.html', locals())
