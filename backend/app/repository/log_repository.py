from sqlalchemy.orm import Session
from app.models.survey import LogAB


def create_log(db: Session, response_id: int, data: dict | None = None):
    log = LogAB(response_id=response_id, data=data or {})
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


def delete_log(db: Session, id: int):
    found = db.query(LogAB).filter_by(id=id).first()
    if not found:
        return None
    db.delete(found)
    db.commit()
    return found
