from pydantic import BaseModel


class LogCreate(BaseModel):
    response_id: int


class LogResponse(BaseModel):
    id: int
    response_id: int
    accesses: int
    dropouts: int
    accessibility_interactions: int

    class Config:
        from_attributes = True
