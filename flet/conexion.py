import mysql.connector

def obtener_conexion():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="a1b2c3d4_",
            database="sistema_cultivos"
    )