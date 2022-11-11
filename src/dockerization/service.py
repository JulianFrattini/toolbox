import uvicorn
from fastapi import FastAPI, Request

from src.util.helper import get_key

app = FastAPI(
    title="Dockerization Test",
    version="1.0.0"
)


@app.get("/health")
def health():
    key: str = get_key()
    return {
        "status": "up",
        "key": key
    }


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
