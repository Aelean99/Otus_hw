import uvicorn
from fastapi import FastAPI, Header, exceptions, Depends

app = FastAPI()


@app.get("/ping", status_code=200, summary="Not for test the connection", tags=["get"])
async def ping():
    return {"message": "pong"}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
