import mysql.connector

# Establecer la conexión con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="ejercicio_usuario"
)

# Verificar si la conexión fue exitosa
if conexion.is_connected():
    print("Conexión exitosa a la base de datos MySQL")

    # Crear un cursor para ejecutar consultas
    cursor = conexion.cursor()

    # Ejecutar una consulta
    cursor.execute("SELECT * FROM usuarios")

    # Obtener los resultados de la consulta
    resultados = cursor.fetchall()

    # Imprimir los resultados
    for fila in resultados:
        print(fila)

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
else:
    print("Error al conectar a la base de datos MySQL")
