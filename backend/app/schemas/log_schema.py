from pydantic import BaseModel


class LogCreate(BaseModel):
    response_id: int
    data: dict


class LogResponse(BaseModel):
    id: int
    response_id: int
    data: dict

    class Config:
        from_attributes = True
