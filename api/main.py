from fastapi import FastAPI
from backendpython import personas 

app = FastAPI()

app.include_router(personas.router)

@app.get("/")
async def root():
    return {"message":"Hello World"}

