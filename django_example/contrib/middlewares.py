import uuid
import time

from http import HTTPStatus
from typing import Any, Callable
from django.http import HttpRequest
from django.http import JsonResponse

from django_example.contrib.errors import APIError


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

    def process_exception(self, request: HttpRequest, exception: Any):
        if isinstance(exception, APIError):
            status = exception.status
            code = exception.code
            error = exception.msg
        else:
            status = HTTPStatus.INTERNAL_SERVER_ERROR
            code = APIError.ErrorCode.UNDEFINED
            error = str(exception)

        return JsonResponse(
            data={
                "error": error,
                "code": code,
            },
            status=status,
        )
