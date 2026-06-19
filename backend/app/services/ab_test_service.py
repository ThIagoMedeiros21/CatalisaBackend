from threading import Lock

CATALISA = "https://catalisa-frontend-mt.vercel.app"
FORMS = "https://forms.gle/m1maAYUjStB4bjaD6"

_counter = 0
_lock = Lock()


def next_id() -> int:
    global _counter
    with _lock:
        _counter += 1
        return _counter


def target_url_for(user_id: int) -> str | None:
    return CATALISA if user_id % 2 == 0 else FORMS


def counts() -> dict:
    with _lock:
        total = _counter
    catalisa = total // 2
    forms = total - catalisa
    return {
        "total": total,
        "targets": [
            {"target": "catalisa", "url": CATALISA, "visitors": catalisa},
            {"target": "forms", "url": FORMS, "visitors": forms},
        ],
    }
