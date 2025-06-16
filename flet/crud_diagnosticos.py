# crud_diagnosticos.py

import mysql.connector
from conexion import obtener_conexion

def insertar_diagnostico(nombre_foto, fecha, nombre_enfermedad, info_detallada, tratamiento, correo_usuario):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="a1b2c3d4_",
        database="sistema_cultivos"
    )
    cursor = conexion.cursor()
    consulta = """
        INSERT INTO informacion 
        (nombre_foto, fecha, nombre_enfermedad, info_detallada, tratamiento, correo_usuario)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (nombre_foto, fecha, nombre_enfermedad, info_detallada, tratamiento, correo_usuario)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_diagnosticos(correo_usuario):
    conn = None
    cursor = None
    try:
        conn = obtener_conexion()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM informacion WHERE correo_usuario = %s"
        cursor.execute(query, (correo_usuario,))
        resultados = cursor.fetchall()
        return resultados
    except mysql.connector.Error as err:
        print(f"Error al obtener informacion: {err}")
        return []
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()