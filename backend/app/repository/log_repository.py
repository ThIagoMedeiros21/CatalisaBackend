from sqlalchemy.orm import Session
from app.models.survey import LogAB


def create_log(db: Session, response_id: int, session_id: str | None = None):
    log = LogAB(response_id=response_id, session_id=session_id)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


def get_log(db: Session, id: int):
    return db.query(LogAB).filter_by(id=id).first()


def get_all_log(db: Session):
    return db.query(LogAB).all()


def get_by_response(db: Session, response_id: int):
    return db.query(LogAB).filter_by(response_id=response_id).first()


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


def update_log(db: Session, id: int, accesses: int, dropouts: int, accessibility_interactions: int):
    found = db.query(LogAB).filter_by(id=id).first()
    if not found:
        return None
    found.accesses = accesses
    found.dropouts = dropouts
    found.accessibility_interactions = accessibility_interactions
    db.commit()
    return found
