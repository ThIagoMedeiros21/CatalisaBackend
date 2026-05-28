from app.models.survey import Pesquisa
from sqlalchemy.orm import Session
from app.enums import RespondentType

def create_survey(db: Session, title: str, respondent_type: RespondentType, is_active: bool = True):
    survey = Pesquisa(title=title, respondent_type=respondent_type, is_active=is_active)
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey

def get_survey(db: Session, id: int):
    return db.query(Pesquisa).filter_by(id = id).first()

def get_all_survey(db: Session):
    return db.query(Pesquisa).all()

def found_by_title_and_respondent(db: Session, title: str, respondent_type: RespondentType):
    return db.query(Pesquisa).filter(
    Pesquisa.title == title,
    Pesquisa.respondent_type == respondent_type
    ).first()

def update_survey(db: Session, id: int, title: str, respondent_type: RespondentType, is_active: bool):
    found = db.query(Pesquisa).filter_by(id = id).first()
    if not found:
        return None
    found.title = title
    found.respondent_type = respondent_type
    found.is_active = is_active
    db.commit()
    return found

def delete_survey(db: Session, id:int):
    found = db.query(Pesquisa).filter_by(id=id).first()
    if not found:
        return None
    db.delete(found)
    db.commit()
    return found