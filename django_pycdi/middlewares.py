from pycdi.core import DEFAULT_CONTAINER
from pycdi.core import INJECT_ARGS
from pycdi.core import INJECT_KWARGS


class CDIMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        self.container = DEFAULT_CONTAINER

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        inject_kwargs = getattr(view_func, INJECT_KWARGS, False)
        if not inject_kwargs:
            return None
        inject_args = getattr(view_func, INJECT_ARGS, False)
        sub_container = self.container.sub_container(request, **view_kwargs)
        if len(inject_args) > 0 or 'request' in inject_kwargs:
            return sub_container.call(view_func, *view_args, **view_kwargs)
        else:
            return sub_container.call(view_func, request, *view_args, **view_kwargs)
