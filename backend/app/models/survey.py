from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.dialects.postgresql import JSONB
from app.enums import RespondentType

class Pesquisa(Base):
    
    __tablename__ = "surveys"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    respondent_type = Column(Enum(RespondentType), nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

class Resposta(Base):

    __tablename__ = "responses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)
    answered_data = Column(JSONB, nullable=False)
    submitted_at = Column(DateTime, default=func.now(), nullable=False)

class LogAB(Base):

    __tablename__ = "log_a_b"

    id = Column(Integer, primary_key=True, autoincrement=True)
    response_id = Column(Integer, ForeignKey("responses.id"), nullable=False)
    session_id = Column(String(255), nullable=True)
    accesses = Column(Integer, default=0, nullable=False)
    dropouts = Column(Integer, default=0, nullable=False)
    accessibility_interactions = Column(Integer, default=0, nullable=False)