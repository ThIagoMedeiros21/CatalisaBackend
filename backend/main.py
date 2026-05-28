from fastapi import FastAPI
from app.routers import survey_router
app = FastAPI()

@app.get("/")
def hello():
    return {"status": "Catalisa backend rodando!"}

app.include_router(survey_router.router, prefix="/surveys", tags=["Surveys"])