from sqlalchemy.orm import Session
from app.models.survey import Respostas

def create_responses(db: Session, survey_id: int, answered_data: dict):
    responses = Respostas(survey_id = survey_id, answered_data = answered_data)
    db.add(responses)
    db.commit()
    db.refresh(responses)
    return responses

def get_responses(db: Session, id: int):
    return db.query(Respostas).filter_by(id=id).first()

def get_all_responses(db: Session):
    return db.query(Respostas).all()

def delete_responses(db: Session, id: int):
    responses = db.query(Respostas).filter_by(id=id).first()
    if not responses:
        return None
    db.delete(responses)
    db.commit()
    return responses
