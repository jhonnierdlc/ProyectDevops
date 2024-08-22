import psycopg2
from fastapi import HTTPException

def get_db_connection():
    try:
        connection = psycopg2.connect(
            host='postgresql',
            port='5432',
            user='root',
            password='root',
            database='personas'
        )
        return connection
    except Exception as ex:
        print(f"Error: {ex}")
        raise HTTPException(status_code=500, detail="Error al conectar a la base de datos")
    
def check_and_create_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Consulta para verificar si la tabla 'personas' existe
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_name = 'personas'
            );
        """)
        table_exists = cursor.fetchone()[0]

        # Si la tabla no existe, la creamos
        if not table_exists:
            cursor.execute("""
                CREATE TABLE personas (
                    tipo_identificacion VARCHAR(50),
                    numero_identificacion VARCHAR(50) PRIMARY KEY,
                    nombre1 VARCHAR(50),
                    nombre2 VARCHAR(50),
                    apellido1 VARCHAR(50),
                    apellido2 VARCHAR(50),
                    sexo VARCHAR(2),
                    fecha_nacimiento DATE
                );
            """)
            connection.commit()
            print("Tabla 'personas' creada exitosamente.")
        else:
            print("La tabla 'personas' ya existe.")
    except Exception as ex:
        raise HTTPException(status_code=500, detail=f"Error al verificar o crear la tabla: {ex}")
    finally:
        cursor.close()
        connection.close()