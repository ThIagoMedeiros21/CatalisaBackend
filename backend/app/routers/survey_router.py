from fastapi import APIRouter, HTTPException
from app.services import survey_service
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import Response
from app.database import get_db
from backend.app.schemas.survey_schema import SurveyCreate
from backend.app.schemas.survey_schema import SurveyUpdate

router = APIRouter()

@router.get("")
def get_all_surveys(db: Session = Depends(get_db)):
    return survey_service.get_all_survey(db)

@router.get("/{id}")
def get_survey(id: int, db: Session = Depends(get_db)):
    
    survey = survey_service.get_survey(db, id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey não encontrado")
    return survey

@router.delete("/{id}")
def delete_survey(id: int, db: Session = Depends(get_db)):
    survey = survey_service.get_survey(db, id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey não encontrado")
    
    resultado = survey_service.delete_survey(db, id)
    if resultado is None:
        raise HTTPException(status_code=409, detail="Survey possui respostas ou logs vinculados")
    return Response(status_code=204)

@router.post("", status_code=201)
def create_survey(data: SurveyCreate, db: Session = Depends(get_db)):
    resultado = survey_service.create_survey(db, data.title, data.respondent_type, data.is_active)
    if resultado is None:
        raise HTTPException(status_code=409, detail="Survey já existe")
    return resultado

@router.patch("/{id}")
def update_survey(data: SurveyUpdate, id: int, db: Session = Depends(get_db)):
    survey = survey_service.get_survey(db, id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey não encontrado")
    
    resultado = survey_service.update_survey(db, id, data.title, data.respondent_type, data.is_active)
    if resultado is None:
        raise HTTPException(status_code=409, detail="Já existe outro survey com esse título e tipo")
    return resultado