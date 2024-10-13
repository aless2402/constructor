from fastapi import FastAPI
from Api.routers import contact

app = FastAPI()

app.include_router()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0", port=8000)