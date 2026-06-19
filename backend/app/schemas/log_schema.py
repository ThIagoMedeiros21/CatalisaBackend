from pydantic import BaseModel


class LogCreate(BaseModel):
    response_id: int
    session_id: str | None = None


class LogResponse(BaseModel):
    id: int
    response_id: int
    session_id: str | None
    accesses: int
    dropouts: int
    accessibility_interactions: int

    class Config:
        from_attributes = True
