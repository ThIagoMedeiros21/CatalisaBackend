from fastapi import APIRouter, Cookie
from fastapi.responses import RedirectResponse
from app.services import ab_test_service

router = APIRouter()

COOKIE_NAME = "ab_session_id"
COOKIE_MAX_AGE = 60 * 60 * 24 * 7  # 1 semana


@router.get("")
def ab_test_redirect(ab_session_id: str | None = Cookie(default=None)):
    is_new = ab_session_id is None or not ab_test_service.is_valid_session(ab_session_id)
    if is_new:
        ab_session_id = ab_test_service.new_session_id()

    response = RedirectResponse(url=ab_test_service.target_url(), status_code=302)
    if is_new:
        response.set_cookie(
            key=COOKIE_NAME,
            value=ab_session_id,
            max_age=COOKIE_MAX_AGE,
            httponly=False,
            samesite="lax",
            path="/",
        )
    return response
