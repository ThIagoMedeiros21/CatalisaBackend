from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import survey  
from app.repository import responses_repository

def submit(db: Session, title: str, respondent_type, answered_data: dict):

    if not answered_data or not any(v for v in answered_data.values()):
        return None

    try:
        survey = (
            db.execute(
                select(survey)
                .where(survey.title == title, survey.respondent_type == respondent_type)
                .with_for_update()  
            )
            .scalars()
            .first()
        )

        if not survey or not survey.is_active:
            return None

        response = responses_repository.create_responses(db, survey.id, answered_data)
        db.commit()
        return {"survey": survey, "response": response}

    except Exception:
        db.rollback()
        raise