from app.services import responses_services
from app.schemas.responses import ResponsesCreate
from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("")
def get_all_responses(db: Session = Depends(get_db)):
    return responses_services.get_all_responses(db)

@router.get("/{id}")
def get_responses(id: int, db: Session = Depends(get_db)):
    response = responses_services.get_responses(db, id)
    if response is None:
        raise HTTPException(status_code=404, detail="Response não encontrada")
    return response

@router.post("", status_code=201)
def create_responses(data: ResponsesCreate, db: Session = Depends(get_db)):
    resultado = responses_services.create_responses(db, data.survey_id, data.answered_data)
    if resultado is None:
        raise HTTPException(status_code=422, detail="Survey não encontrado, inativo ou dados vazios")
    return resultado

@router.delete("/{id}")
def delete_response(id: int, db: Session = Depends(get_db)):
    response = responses_services.get_responses(db, id)
    if response is None:
        raise HTTPException(status_code=404, detail="Response não encontrada")
    responses_services.delete_responses(db, id)
    return Response(status_code=204)