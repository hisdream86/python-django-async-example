import ujson

from django.http import HttpResponse
from typing import Any, Dict, Optional


class APIResponse(HttpResponse):
    def __init__(self, data: Dict[str, Any] = None, headers: Optional[Dict[str, str]] = {}):
        if not isinstance(data, dict):
            raise TypeError("'data' should be dictionary type")

        data = ujson.dumps(data, ensure_ascii=False)
        super().__init__(content=data, content_type="application/json", headers=headers)
