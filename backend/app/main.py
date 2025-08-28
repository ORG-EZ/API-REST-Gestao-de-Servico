from fastapi import FastAPI
from app.core.config import DEBUG

app = FastAPI(debug=DEBUG)

@app.get("/")
def root():
    return {"message": f"API rodando com DEBUG={DEBUG}"}
