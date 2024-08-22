from fastapi import APIRouter, HTTPException
from backendpython.src.conexion_postgresql import get_db_connection
from backendpython.src.models.persona import Persona


router = APIRouter(prefix="/api/backend-python",
                   tags=["persona-python"],
                   responses={404: {"message": "No encontrado"}})


personas_list = []
    
@router.get("/")
async def root():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM personas")
        personas = cursor.fetchall()
        return [{"tipo_identificacion": p[0], "numero_identificacion": p[1], "nombre1": p[2], "nombre2": p[3], "apellido1": p[4], "apellido2": p[5], "sexo": p[6], "fecha_nacimiento": p[7]} for p in personas]
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error al obtener personas: {ex}")
    finally:
        cursor.close()
        connection.close()

@router.get("/{numero_identificacion}")
async def root(numero_identificacion : str):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM personas WHERE numero_identificacion = %s", (numero_identificacion,))
        persona = cursor.fetchone()
        if persona:
            return {"tipo_identificacion": persona[0], "numero_identificacion": persona[1], "nombre1": persona[2], "nombre2": persona[3], "apellido1": persona[4], "apellido2": persona[5], "sexo": persona[6], "fecha_nacimiento": persona[7]}
        else:
            raise HTTPException(status_code=404, detail="Persona no encontrada")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error al obtener persona: {ex}")
    finally:
        cursor.close()
        connection.close()
    

            
def search_persona(numero_identificacion: int):
    personas = filter(lambda persona: persona.numero_identificacion == numero_identificacion, personas_list)
    try:
        return list(personas)[0]
    except:
        return {"error": "no se encontro"}

@router.post("/", response_model=Persona, status_code=201)
async def add_persona(persona: Persona):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT 1 FROM personas WHERE numero_identificacion = %s", (persona.numero_identificacion,))
        if cursor.fetchone():
            raise HTTPException(status_code=400, detail="El número de identificación ya existe")

        cursor.execute("""
            INSERT INTO personas (tipo_identificacion, numero_identificacion, nombre1, nombre2, apellido1, apellido2, sexo, fecha_nacimiento)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            persona.tipo_identificacion, persona.numero_identificacion, 
            persona.nombre1, persona.nombre2, persona.apellido1, 
            persona.apellido2, persona.sexo, persona.fecha_nacimiento
        ))
        connection.commit()
        return persona
    except Exception as ex:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Error al insertar persona: {ex}")
    finally:
        cursor.close()
        connection.close()
        