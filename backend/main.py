from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging_config import setup_logging
from app.routers import survey_router
from app.routers import logs_router
from app.routers import response_router
from app.routers import submit_router
from app.routers import ab_test_router

setup_logging()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://catalisa-frontend-mt.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def hello():
    return {"status": "Catalisa backend rodando!"}

app.include_router(survey_router.router, prefix="/surveys", tags=["Surveys"])
app.include_router(logs_router.router, prefix="/logs", tags=["Logs"])
app.include_router(response_router.router, prefix="/responses", tags=["Responses"])
app.include_router(submit_router.router, prefix="/submit", tags=["Submit"])
app.include_router(ab_test_router.router, prefix="/ab-test", tags=["AB Test"])