from sqlalchemy.orm import Session
from app.models.survey import LogAB
from app.enums import RespondentType

def create_log(db:Session, survey_id: int, session_id: str, respondent_type: RespondentType):
    log = LogAB(survey_id = survey_id, session_id = session_id, respondent_type = respondent_type)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_log(db: Session, id: int):
    return db.query(LogAB).filter_by(id=id).first()

def get_all_log(db: Session):
    return db.query(LogAB).all()

def get_by_session_survey(db: Session, survey_id: int, session_id: str):
    return db.query(LogAB).filter(
        LogAB.survey_id == survey_id,
        LogAB.session_id == session_id
    ).first()

def increment_access(db: Session, id: int):
    found = db.query(LogAB).filter_by(id=id).first()
    if not found:
        return None
    found.accesses += 1
    db.commit()
    db.refresh(found)
    return found

def increment_dropout(db: Session, id: int):
    found = db.query(LogAB).filter_by(id=id).first()
    if not found:
        return None
    found.dropouts += 1
    db.commit()
    db.refresh(found)
    return found

def increment_accessibility_interaction(db: Session, id: int):
    found = db.query(LogAB).filter_by(id=id).first()
    if not found:
        return None
    found.accessibility_interactions += 1
    db.commit()
    db.refresh(found)
    return found

def delete_log(db: Session, id: int):
    found = db.query(LogAB).filter_by(id=id).first()
    if not found:
        return None
    db.delete(found)
    db.commit()
    return found

def exists_by_survey(db: Session, survey_id: int):
    return db.query(LogAB).filter_by(survey_id=survey_id).first() is not None

def update_log(db: Session, id: int, accesses: int, dropouts: int, accessibility_interactions: int):
    found = db.query(LogAB).filter_by(id=id).first()
    if not found:
        return None
    found.accesses = accesses
    found.dropouts = dropouts
    found.accessibility_interactions = accessibility_interactions
    db.commit()
    return found
     