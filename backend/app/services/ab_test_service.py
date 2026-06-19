import uuid

CATALISA = "https://catalisa-frontend-mt.vercel.app"


def new_session_id() -> str:
    return str(uuid.uuid4())


def is_valid_session(session_id: str) -> bool:
    try:
        uuid.UUID(session_id)
        return True
    except ValueError:
        return False


def target_url() -> str:
    return CATALISA
