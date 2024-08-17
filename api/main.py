from fastapi import FastAPI
from ProyectDevops.api.backendpython import personas 

app = FastAPI()

app.include_router(personas.router)

@app.get("/")
async def root():
    return {"message":"Hello World"}

