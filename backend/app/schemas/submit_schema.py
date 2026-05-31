from pydantic import BaseModel
from app.enums import RespondentType

class SurveyData(BaseModel):
    title: str
    respondent_type: RespondentType

class ResponseData(BaseModel):
    answered_data: dict

class SubmitCreate(BaseModel):
    survey: SurveyData
    response: ResponseData