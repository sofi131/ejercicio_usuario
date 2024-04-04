import faker
import hashlib
import mysql.connector
import requests
import os

# Función para generar el hash MD5 de una cadena
def generar_md5(cadena):
    return hashlib.md5(cadena.encode()).hexdigest()

# Crear un objeto Faker
generador = faker.Faker()

# Para descargar las imágenes ficticias
def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as f:
            f.write(response.content)
        print("Imagen descargada con éxito como", nombre_archivo)
    else:
        print("Error al descargar la imagen:", response.status_code)

def descargar_imagenes_desde_thispersondoesnotexist(num_imagenes):
    url_base = "https://thispersondoesnotexist.com"
    for i in range(1, num_imagenes + 1):
        url = f"{url_base}"
        nombre_archivo = f"datos/imagenes_usuarios/persona_{i}.jpg"
        descargar_imagen(url, nombre_archivo)

if __name__ == "__main__":
    num_imagenes = int(input("Ingrese el número de imágenes que desea descargar: "))
    descargar_imagenes_desde_thispersondoesnotexist(num_imagenes)

# Generar 1000 nombres, correos electrónicos y contraseñas
datos = []
for i in range(1000):
    nombre = generador.name()
    email = generador.email()
    password = '1224'  # Contraseña fija para todos
    password_encriptada = generar_md5(password)  # Encriptar la contraseña
    imagen_url = f'datos/imagenes_usuarios/persona_{i + 1}.jpg'
    datos.append((nombre, email, password_encriptada, imagen_url))

# Establecer la conexión con la base de datos MySQL
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

    # Insertar los datos en la base de datos
    consulta = "INSERT INTO usuarios (nombre, email, password, imagen_url) VALUES (%s, %s, %s, %s)"
    cursor.executemany(consulta, datos)

    # Confirmar la transacción
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()
else:
    print("Error al conectar a la base de datos MySQL")
