# conexion.py
#se añadieron funciones para poderlas reciclar despues y optimizar codigo
import mysql.connector

def obtener_conexion():
    # Establece y retorna una conexión a la base de datos MySQL.
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="a1b2c3d4_", # cambio de contraseña para tu bd
            database="sistema_cultivos" 
        )
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        # Aquí podrías lanzar una excepción o manejar el error de forma más específica
        return None # Retorna None si la conexión falla

def get_user_by_email(email):
    """
    Obtiene los datos de un usuario de la base de datos por su correo electrónico.
    Retorna un diccionario con los datos del usuario si se encuentra, o None si no.
    """
    conn = None
    cursor = None
    try:
        conn = obtener_conexion()
        if not conn: # Si la conexión falló en obtener_conexion()
            return None

        cursor = conn.cursor(dictionary=True) # Para obtener resultados como diccionarios
        query = "SELECT id, nombre, correo, telefono, contraseña FROM usuarios WHERE correo = %s"
        cursor.execute(query, (email,))
        user_data = cursor.fetchone()
        return user_data
    except mysql.connector.Error as err:
        print(f"Error al obtener usuario por email: {err}")
        return None
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def update_user(email, data_to_update):
    """
    Actualiza la información de un usuario existente en la base de datos.
    Solo actualiza los campos 'nombre', 'telefono' y 'contrasena' si están presentes en data_to_update.
    """
    conn = None
    cursor = None
    try:
        conn = obtener_conexion()
        if not conn:
            return False

        cursor = conn.cursor()

        set_clauses = []
        values = []

        if 'nombre' in data_to_update:
            set_clauses.append("nombre = %s")
            values.append(data_to_update['nombre'])
        if 'telefono' in data_to_update:
            set_clauses.append("telefono = %s")
            values.append(data_to_update['telefono'])
        if 'contrasena' in data_to_update: # Solo actualiza la contraseña si se proporcionó una nueva
            set_clauses.append("contrasena = %s")
            values.append(data_to_update['contrasena'])

        if not set_clauses: # Si no hay campos para actualizar
            print("No hay campos para actualizar para el usuario:", email)
            return True # O False, dependiendo de si consideras esto un error

        query = f"UPDATE usuarios SET {', '.join(set_clauses)} WHERE correo = %s"
        values.append(email) # Agrega el email para la cláusula WHERE

        cursor.execute(query, tuple(values))
        conn.commit()
        print(f"Usuario {email} actualizado con éxito en la BD.")
        return True
    except mysql.connector.Error as err:
        print(f"Error al actualizar usuario: {err}")
        if conn:
            conn.rollback() # Revierte los cambios si hay un error
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def create_user(user_data):
    """
    Crea un nuevo usuario en la base de datos.
    Ideal para la función de registro.
    """
    conn = None
    cursor = None
    try:
        conn = obtener_conexion()
        if not conn:
            return False

        cursor = conn.cursor()
        query = """
            INSERT INTO usuarios (nombre, correo, telefono, contrasena)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (user_data['nombre'], user_data['correo'], user_data['telefono'], user_data['contrasena']))
        conn.commit()
        print(f"Usuario {user_data['correo']} creado con éxito en la BD.")
        return True
    except mysql.connector.Error as err:
        if err.errno == 1062: # Código de error MySQL para entrada duplicada (UNIQUE constraint)
            print(f"Error: El correo {user_data['correo']} ya está registrado.")
        else:
            print(f"Error al crear usuario: {err}")
        if conn:
            conn.rollback()
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def verify_login(email, password):
    """
    Verifica las credenciales de un usuario para el inicio de sesión.
    ¡ADVERTENCIA! Almacenar contraseñas sin hash es inseguro.
    Considera usar bcrypt o Argon2 para hashear contraseñas en un entorno de producción.
    """
    conn = None
    cursor = None
    try:
        conn = obtener_conexion()
        if not conn:
            return False

        cursor = conn.cursor(dictionary=True)
        query = "SELECT contrasena FROM usuarios WHERE correo = %s"
        cursor.execute(query, (email,))
        user_record = cursor.fetchone()
        if user_record and user_record['contrasena'] == password: # Compara la contraseña directamente (inseguro para producción)
            return True
        return False
    except mysql.connector.Error as err:
        print(f"Error al verificar login: {err}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()