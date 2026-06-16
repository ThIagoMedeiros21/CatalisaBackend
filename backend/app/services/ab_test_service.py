import os
from threading import Lock

_counter = 0
_lock = Lock()


def next_id() -> int:
    global _counter
    with _lock:
        _counter += 1
        return _counter


def target_url_for(user_id: int) -> str | None:
    even_url = os.getenv("AB_URL_EVEN")
    odd_url = os.getenv("AB_URL_ODD")
    if not even_url or not odd_url:
        return None
    return even_url if user_id % 2 == 0 else odd_url
