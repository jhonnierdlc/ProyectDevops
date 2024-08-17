from fastapi import APIRouter, HTTPException
from db.models.persona import Persona



router = APIRouter(prefix="/persona",
                   tags=["persona-python"],
                   responses={404: {"message": "No encontrado"}})

personas_list = []
    
@router.get("/")
async def root():
    return personas_list

@router.get("/{tipo_identificacion}")
async def root(numero_identificacion : int):
    personas = filter(lambda persona: persona.numero_identificacion == numero_identificacion, personas_list)
    try:
        return list(personas)[0]
    except:
        return {"error": "no se encontro"}
    
    
@router.post("/", response_model=Persona, status_code=201)
async def persona(persona: Persona):
    if type(search_persona(persona.numero_identificacion)) == Persona:
        raise HTTPException(status_code=404, detail="la persona ya existe")
   
    personas_list.append(persona)
    return persona
            
def search_persona(numero_identificacion: int):
    personas = filter(lambda persona: persona.numero_identificacion == numero_identificacion, personas_list)
    try:
        return list(personas)[0]
    except:
        return {"error": "no se encontro"}
