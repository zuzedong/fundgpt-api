from fastapi import FastAPI

app = FastAPI(
    title="FundGPT API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "FundGPT API is running"
    }

@app.get("/fund/{code}")
def fund(code: str):
    return {
        "code": code,
        "status": "success",
        "estimate": None,
        "message": "FundGPT API is working."
    }
