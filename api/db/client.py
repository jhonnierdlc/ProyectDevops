import psycopg2

# Establecer la conexión con la base de datos
try:
    connection = psycopg2.connect(
        host="localhost",    
        database="personas",  
        user="root",      
        password="root" 
    )

    # Crear un cursor
    cursor = connection.cursor()

    # Ejecutar una consulta
    cursor.execute("SELECT version();")

    # Obtener el resultado
    record = cursor.fetchone()
    print(f"Conectado a - {record}\n")

except Exception as error:
    print(f"Error al conectarse a PostgreSQL: {error}")
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Conexión a PostgreSQL cerrada")