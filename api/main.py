from fastapi import FastAPI
from backendpython import personas
from backendpython.src.conexion_postgresql import check_and_create_table

app = FastAPI()

check_and_create_table()

app.include_router(personas.router)

@app.get("/")
async def root():
    return {"message":"Hello World"}

