import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import OperationalError
from fastapi import HTTPException

DATABASE_URL = os.environ["DATABASE_URL"]
engine = create_engine(DATABASE_URL)

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