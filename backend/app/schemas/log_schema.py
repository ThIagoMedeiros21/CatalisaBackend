from pydantic import BaseModel
from app.enums import RespondentType


class LogCreate(BaseModel):
    survey_id: int
    session_id: str
    respondent_type: RespondentType


class LogResponse(BaseModel):
    id: int
    survey_id: int
    session_id: str
    respondent_type: RespondentType
    accesses: int
    dropouts: int
    accessibility_interactions: int

    class Config:
        from_attributes = True