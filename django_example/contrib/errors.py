from enum import IntEnum
from http import HTTPStatus


class APIError(Exception):
    class ErrorCode(IntEnum):
        UNDEFINED = 5000

    def __init__(self, msg="Server error", status=HTTPStatus.INTERNAL_SERVER_ERROR, code=ErrorCode.UNDEFINED.value):
        super().__init__(msg)
        self.status = status
        self.code = code
        self.msg = msg


class BadRequest(APIError):
    class ErrorCode(IntEnum):
        BAD_REQUEST = 4000
        INVALID_VALUE = 4001

    def __init__(self, msg="Invalid request", code=ErrorCode.BAD_REQUEST.value):
        super().__init__(msg, HTTPStatus.BAD_REQUEST, code)


class NotFound(APIError):
    class ErrorCode(IntEnum):
        NOT_FOUND = 4040
        OBJECT_NOT_FOUND = 4041

    def __init__(self, msg="Resource does not exist", code=ErrorCode.NOT_FOUND.value):
        super().__init__(msg, HTTPStatus.NOT_FOUND, code)


class InternalServerError(APIError):
    class ErrorCode(IntEnum):
        SERVER_ERROR = 5000

    def __init__(self, msg="Internal Server Error", code=ErrorCode.SERVER_ERROR.value):
        super().__init__(msg, HTTPStatus.INTERNAL_SERVER_ERROR, code)
