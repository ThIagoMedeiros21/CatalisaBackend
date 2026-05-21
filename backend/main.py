from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"status": "Catalisa backend rodando!"}