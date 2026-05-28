from fastapi import APIRouter, HTTPException
from app.services import survey_service
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi import Response
from app.database import get_db
from app.schemas.survey import SurveyCreate
from app.schemas.survey import SurveyUpdate

router = APIRouter()

@router.get("/getallsurveys")
def get_all_surveys(db: Session = Depends(get_db)):
    return survey_service.get_all_survey(db)

@router.get("/getsurvey/{id}")
def get_survey(id: int, db: Session = Depends(get_db)):

    survey = survey_service.get_survey(db, id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey não encontrado")
    
    else:
        return survey
    
@router.delete("/deletesurvey/{id}")
def delete_survey(id: int, db: Session = Depends(get_db)):
    survey = survey_service.get_survey(db, id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey não encontrado")
    else:
        survey_service.delete_survey(db,id)
        return Response(status_code=204)

@router.post("/createsurvey")
def create_survey(data: SurveyCreate, db: Session = Depends(get_db)):
    resultado = survey_service.create_survey(db, data.title, data.respondent_type, data.is_active)
    if resultado is None:
        raise HTTPException(status_code=409, detail="Survey já existe") 
    return resultado

@router.put("/updatesurvey/{id}")
def update_survey(data: SurveyUpdate, id:int, db: Session = Depends(get_db),):
    survey = survey_service.get_survey(db, id)
    if survey is None:
        raise HTTPException(status_code=404, detail="Survey não encontrado")
    
    else:
        up = survey_service.update_survey(db, id, data.title, data.respondent_type, data.is_active)
        return up