from sqlalchemy.orm import Session
from app.repository import log_repository
from app.repository import survey_repository

def create_log(db:Session, survey_id: int, session_id: str, respondent_type: RespondentType):
    survey = survey_repository.get_survey(db, survey_id)
    if not survey:
        return None
    
     
def get_log(db: Session, id: int):
    ...

def get_all_log(db: Session):
    ...

def increment_access(db: Session, id: int):
    ...

def increment_dropout(db: Session, id: int):
    ...

def increment_accessibility_interaction(db: Session, id: int):
    ...

def delete_log(db: Session, id: int):
    ...