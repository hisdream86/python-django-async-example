import asyncio

from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class AsyncAPIView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AsyncAPIView, self).dispatch(request, *args, **kwargs)

    @classmethod
    def as_view(cls, **kwargs):
        view = super().as_view(**kwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view
