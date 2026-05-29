from sqlalchemy.orm import Session
from app.repository import log_repository
from app.repository import survey_repository
from app.enums import RespondentType

def create_log(db: Session, survey_id: int, session_id: str, respondent_type: RespondentType, accesses: int = 0, dropouts: int = 0, accessibility_interactions: int = 0):
    survey = survey_repository.get_survey(db, survey_id)
    if not survey:
        return None
    if not survey.is_active:
        return None

    existing = log_repository.get_by_session_survey(db, survey_id, session_id)
    if existing:
        return log_repository.update_log(db, existing.id, accesses, dropouts, accessibility_interactions)
    return log_repository.create_log(db, survey_id, session_id, respondent_type, accesses, dropouts, accessibility_interactions)

def get_log(db: Session, id: int):
    return log_repository.get_log(db, id)

def get_all_log(db: Session):
    return log_repository.get_all_log(db)

def increment_access(db: Session, id: int):
    if not log_repository.get_log(db, id):
        return None
    return log_repository.increment_access(db, id)

def increment_dropout(db: Session, id: int):
    if not log_repository.get_log(db, id):
        return None
    return log_repository.increment_dropout(db, id)

def increment_accessibility_interaction(db: Session, id: int):
    if not log_repository.get_log(db, id):
        return None
    return log_repository.increment_accessibility_interaction(db, id)

def delete_log(db: Session, id: int):
    return log_repository.delete_log(db, id)