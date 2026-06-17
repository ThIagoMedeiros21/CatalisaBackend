from fastapi import APIRouter, Cookie, HTTPException
from fastapi.responses import RedirectResponse
from app.services import ab_test_service

router = APIRouter()

COOKIE_NAME = "ab_user_id"
COOKIE_MAX_AGE = 60 * 60 * 24 * 7 # 1 semana


def _parse_cookie(value: str | None) -> int | None:
    if value is None:
        return None
    try:
        return int(value)
    except ValueError:
        return None


@router.get("")
def ab_test_redirect(ab_user_id: str | None = Cookie(default=None)):
    user_id = _parse_cookie(ab_user_id)
    is_new = user_id is None
    if is_new:
        user_id = ab_test_service.next_id()

    target = ab_test_service.target_url_for(user_id)
    if target is None:
        raise HTTPException(status_code=500, detail="AB_URL_EVEN/AB_URL_ODD não configurados")

    response = RedirectResponse(url=target, status_code=302)
    if is_new:
        response.set_cookie(
            key=COOKIE_NAME,
            value=str(user_id),
            max_age=COOKIE_MAX_AGE,
            httponly=True,
            samesite="lax",
            path="/",
        )
    return response
