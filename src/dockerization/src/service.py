import uvicorn
from fastapi import FastAPI, Request

app = FastAPI(
    title="Dockerization Test",
    version="1.0.0"
)

@app.get("/health")
def health():
    return {"status": "up"}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')