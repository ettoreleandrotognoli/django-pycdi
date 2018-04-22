from django.conf import settings
from pycdi.core import DEFAULT_CONTAINER
from pycdi.core import INJECT_ARGS
from pycdi.core import INJECT_KWARGS

CDI_NAME = getattr(settings, 'CDI_NAME', 'cdi')


class CDIMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        self.container = DEFAULT_CONTAINER

    def __call__(self, request):
        sub_container = self.container.sub_container(request)
        setattr(request, CDI_NAME, sub_container)
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        sub_container = getattr(request, CDI_NAME)
        for k, v in view_kwargs.items():
            sub_container.register_instance(v, context=k)
        inject_kwargs = getattr(view_func, INJECT_KWARGS, False)
        if not inject_kwargs:
            return None
        inject_args = getattr(view_func, INJECT_ARGS, False)

        if len(inject_args) > 0 or 'request' in inject_kwargs:
            return sub_container.call(view_func, *view_args, **view_kwargs)
        else:
            return sub_container.call(view_func, request, *view_args, **view_kwargs)
