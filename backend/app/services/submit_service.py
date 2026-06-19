from sqlalchemy.orm import Session
from app.repository import survey_repository, responses_repository
from app.repository import log_repository


def submit(db: Session, title: str, respondent_type, answered_data: dict):
    survey = survey_repository.found_by_title_and_respondent(db, title, respondent_type)
    if not survey:
        return None
    if not survey.is_active:
        return None
    if not answered_data or not any(v for v in answered_data.values()):
        return None

    response = responses_repository.create_responses(db, survey.id, answered_data)
    log_repository.create_log(db, response.id)

    return {"survey": survey, "response": response}
