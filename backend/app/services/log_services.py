from sqlalchemy.orm import Session
from app.repository import log_repository
from app.repository import responses_repository


def create_log(db: Session, response_id: int, session_id: str | None = None):
    response = responses_repository.get_responses(db, response_id)
    if not response:
        return None

    existing = log_repository.get_by_response(db, response_id)
    if existing:
        return existing

    return log_repository.create_log(db, response_id, session_id)


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
