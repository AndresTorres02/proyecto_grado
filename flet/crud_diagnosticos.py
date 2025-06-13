# crud_diagnosticos.py

import mysql.connector
from conexion import obtener_conexion

def insertar_diagnostico(numero_foto, nombre_foto, fecha, nombre_enfermedad, info_detallada, tratamiento):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="a1b2c3d4_",
        database="sistema_cultivos"
    )
    cursor = conexion.cursor()
    consulta = """
        INSERT INTO informacion 
        (numero_foto, nombre_foto, fecha, nombre_enfermedad, info_detallada, tratamiento)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (numero_foto, nombre_foto, fecha, nombre_enfermedad, info_detallada, tratamiento)
    cursor.execute(consulta, valores)
    conexion.commit()
    cursor.close()
    conexion.close()

def obtener_diagnosticos():
    conn = None
    cursor = None
    try:
        conn = obtener_conexion()
        if not conn:
            return []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM informacion"
        cursor.execute(query)
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