from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.submit_schema import SubmitCreate
from app.services import submit_service

router = APIRouter()

@router.post("", status_code=201)
def submit(data: SubmitCreate, db: Session = Depends(get_db)):
    resultado = submit_service.submit(
        db,
        data.survey.title,
        data.survey.respondent_type,
        data.response.answered_data
    )
    if resultado is None:
        raise HTTPException(status_code=422, detail="Survey não encontrado, inativo ou dados vazios")
    return resultado