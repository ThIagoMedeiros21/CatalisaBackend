import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import OperationalError
from fastapi import HTTPException

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError(
        "Missing required environment variable 'DATABASE_URL'. "
        "Set it before starting the application."
    )

engine = create_engine(
    DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800,
    pool_pre_ping=True,  
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db

    except OperationalError:
        raise HTTPException(
            status_code=503,
            detail="Não foi possível conectar ao banco de dados."
        )

    finally:
        db.close()