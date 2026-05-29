from pydantic import BaseModel
from app.enums import RespondentType
from datetime import datetime

class SurveyCreate(BaseModel):
    title: str
    respondent_type: RespondentType
    is_active: bool = True

class SurveyUpdate(BaseModel):
    title: str
    respondent_type: RespondentType
    is_active: bool

class SurveyResponse(BaseModel):
    id: int
    title: str
    respondent_type: RespondentType
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True