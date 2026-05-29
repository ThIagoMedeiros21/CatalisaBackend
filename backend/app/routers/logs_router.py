from app.services import log_services
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("")
def get_all_logs(db: Session = Depends(get_db)):
    return log_services.get_all_log(db)

@router.get("/{id}")
def get_log(id: int, db: Session = Depends(get_db)):
    log = log_services.get_log(id)
    if log is None:
        raise HTTPException(status_code=404, detail = "Log não encontrado")
    
    return log

@router.delete("/{id}")
def delete_log(id: int, db: Session = Depends(get_db)):
    log = log_services.delete_log(db, id)
    if log is None:
        raise HTTPException(status_code = 404, detail = "Log não encontrado")

    return log

@router.post("", status_code=201)
def create_log(data: LogCreate, db: Session = Depends(get_db)):
    resultado = log_services.create_log(db, data.survey_id, data.session_id, data.respondent_type)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Survey não encontrado ou inativo")
    return resultado

@router.patch("/{id}/access")
def increment_access(id: int, db: Session = Depends(get_db)):
    resultado = log_services.increment_access(db, id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Log não encontrado")
    return resultado

@router.patch("/{id}/dropout")
def increment_dropout(id: int, db: Session = Depends(get_db)):
    resultado = log_services.increment_dropout(db, id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Log não encontrado")
    return resultado

@router.patch("/{id}/accessibility")
def increment_accessibility_interaction(id: int, db: Session = Depends(get_db)):
    resultado = log_services.increment_accessibility_interaction(db, id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="Log não encontrado")
    return resultado
