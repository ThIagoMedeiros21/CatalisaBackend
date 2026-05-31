from pydantic import BaseModel
from datetime import datetime


class ResponsesCreate(BaseModel):
    survey_id: int
    answered_data: dict


class ResponsesResponse(BaseModel):
    id: int
    survey_id: int
    answered_data: dict
    submitted_at: datetime

    class Config:
        from_attributes = True