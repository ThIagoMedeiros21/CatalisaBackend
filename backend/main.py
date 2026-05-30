from fastapi import FastAPI
from app.routers import survey_router
from app.routers import logs_router
from app.routers import response_router

app = FastAPI()

@app.get("/")
def hello():
    return {"status": "Catalisa backend rodando!"}

app.include_router(survey_router.router, prefix="/surveys", tags=["Surveys"])
app.include_router(logs_router.router, prefix="/logs", tags=["Logs"])
app.include_router(response_router.router, prefix="/responses", tags=["Responses"])