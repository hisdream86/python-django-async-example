import uuid
import time
import traceback
import ujson


from http import HTTPStatus
from typing import Optional
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.conf import settings

from django_example.contrib.errors import APIError, BadRequest
from django.utils.deprecation import MiddlewareMixin


class APIMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest) -> Optional[HttpResponse]:
        request.start = time.time()
        request.request_id = str(uuid.uuid4())

        try:
            if request.body and request.content_type == "application/json":
                request.data = ujson.loads(request.body)
            else:
                request.data = {}
        except ujson.JSONDecodeError:
            raw_body = request.body.decode("utf-8")
            return self.process_exception(request, BadRequest(f"Invalid JSON string '{raw_body}'"))

    def process_response(self, request: HttpRequest, response: HttpResponse) -> HttpResponse:
        request.end = time.time()
        response["request-id"] = request.request_id
        return response

    def process_exception(self, request: HttpRequest, exception: Exception) -> JsonResponse:
        if isinstance(exception, APIError):
            status = exception.status
            code = exception.code
            error = exception.msg
        else:
            status = HTTPStatus.INTERNAL_SERVER_ERROR
            code = APIError.ErrorCode.UNDEFINED
            error = str(exception)

        if status > 500 and settings.DEBUG:
            traceback.print_exc()

        return JsonResponse(data={"error": error, "code": code}, status=status)
