from sqlalchemy.orm import Session
from app.repository import log_repository
from app.repository import responses_repository


def create_log(db: Session, response_id: int, data: dict):
    response = responses_repository.get_responses(db, response_id)
    if not response:
        return None

    existing = log_repository.get_by_response(db, response_id)
    if existing:
        return log_repository.update_data(db, existing.id, data)

    return log_repository.create_log(db, response_id, data)


def get_log(db: Session, id: int):
    return log_repository.get_log(db, id)


def get_all_log(db: Session):
    return log_repository.get_all_log(db)


def delete_log(db: Session, id: int):
    return log_repository.delete_log(db, id)
