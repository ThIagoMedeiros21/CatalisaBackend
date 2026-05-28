from sqlalchemy.orm import Session
from app.repository import survey_repository
from app.enums import RespondentType

def create_survey(db: Session, title: str, respondent_type: RespondentType, is_active: bool = True):
    if survey_repository.found_by_title_and_respondent(db, title, respondent_type) is not None:
        return None
    
    else:
        return survey_repository.create_survey(db, title, respondent_type, is_active)
    
def get_survey(db: Session, id: int):
    return survey_repository.get_survey(db, id)

def get_all_survey(db: Session):
    return survey_repository.get_all_survey(db)

def update_survey(db: Session, id: int, title: str, respondent_type: RespondentType, is_active: bool):
    return survey_repository.update_survey(db, id, title, respondent_type, is_active)

def delete_survey(db: Session, id:int):
    return survey_repository.delete_survey(db, id)
    