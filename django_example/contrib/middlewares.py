import uuid
import time

from typing import Callable
from django.http import HttpRequest
from django.http import JsonResponse


class APIMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        request.request_id = str(uuid.uuid4())
        request.start = time.time()

        response = self.get_response(request)

        response["request-id"] = request.request_id
        request.end = time.time()

        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        return JsonResponse(
            data={
                "message": str(exception),
            }
        )
