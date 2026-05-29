from sqlalchemy.orm import Session
from app.repository import responses_repository
from app.repository import survey_repository

def create_responses(db: Session, survey_id: int, answered_data: dict):
    survey = survey_repository.get_survey(db, survey_id)
    if not survey:
        return None
    if not survey.is_active:
        return None
    if not answered_data or not any(v for v in answered_data.values()):
        return None
    return responses_repository.create_responses(db, survey_id, answered_data)

def get_responses(db: Session, id: int):
    return responses_repository.get_responses(db, id)

def get_all_responses(db: Session):
    return responses_repository.get_all_responses(db)

def delete_responses(db: Session, id: int):
    return responses_repository.delete_responses(db, id)