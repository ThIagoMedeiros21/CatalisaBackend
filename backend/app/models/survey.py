from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from app.database import Base
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Enum
from app.enums import RespondentType

class Pesquisa(Base):
    
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    respondent_type = Column(Enum(RespondentType))
    created_at = Column(DateTime)
    is_active = Column(Boolean)

class Resposta(Base):

    __tablename__ = "responses"

    id = Column(Integer, primary_key=True)
    survey_id = Column(ForeignKey("surveys.id"))
    answered_data = Column(JSONB)
    submitted_at = Column(DateTime)

class LogAB(Base):
    
    __tablename__ = "log_a_b"

    id = Column(Integer, primary_key=True)
    survey_id = Column(ForeignKey("surveys.id"))
    session_id = Column(String)
    respondent_type = Column(Enum(RespondentType))
    accesses = Column(Integer)
    dropouts = Column(Integer)
    accessibility_interactions = Column(Integer)

