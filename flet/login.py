# Importar el módulo flet para crear la interfaz gráfica
import flet as ft

# Importar el conector para interactuar con MySQL
import mysql.connector

# Función principal que crea la vista de login
def login_view(page: ft.Page, go_to_registrar, go_to_menu, go_to_reset):
    
    # Función que navega hacia la vista de registro cuando se presiona el botón "Regístrate"
    def ir_a_registro(e):
        go_to_registrar()

    # Función para establecer la conexión con la base de datos MySQL
    def conectar_bd():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="a1b2c3d4_", #cambie la contraseña del conector para que me sirviera
            database="sistema_cultivos"
        )

    def ir_a_recuperacion(e):
        go_to_reset()

    # Campo para ingresar el correo electrónico
    correo = ft.TextField(label="Escribe tu correo", text_style=ft.TextStyle(color="black"), border_color="black")
    # Texto para mostrar errores relacionados con el correo
    correo_error = ft.Text("", color="red", size=12)

    # Campo para ingresar la contraseña (modo oculto)
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, text_style=ft.TextStyle(color="black"), border_color="black")
    # Texto para mostrar errores relacionados con la contraseña
    contraseña_error = ft.Text("", color="red", size=12)

    # Cuadro de diálogo para mensajes emergentes (no usado actualmente)
    dialog = ft.AlertDialog()

    # Función para validar el login cuando se presiona el botón LOGIN
    def validar_login(e):
        # Limpiar los colores de los bordes y mensajes de error anteriores
        correo.border_color = "black"
        contraseña.border_color = "black"
        correo_error.value = ""
        contraseña_error.value = ""

        # Verificar si los campos están vacíos
        campos_vacios = False
        if not correo.value.strip():  # Si el campo correo está vacío
            correo.border_color = "red"
            correo_error.value = "Este campo es obligatorio"
            campos_vacios = True

        if not contraseña.value.strip():  # Si el campo contraseña está vacío
            contraseña.border_color = "red"
            contraseña_error.value = "Este campo es obligatorio"
            campos_vacios = True

        # Si algún campo está vacío, se detiene la ejecución
        if campos_vacios:
            page.update()  # Actualiza la vista para reflejar los errores
            return

        # Conectar a la base de datos
        conn = conectar_bd()
        cursor = conn.cursor()

        # Consultar si el correo existe en la base de datos
        cursor.execute("SELECT contraseña FROM usuarios WHERE correo = %s", (correo.value,))
        result = cursor.fetchone()  # Obtiene una sola fila

        # Validar existencia del correo y veracidad de la contraseña
        if result is None:
            correo.border_color = "red"
            correo_error.value = "El correo no está registrado"
        elif result[0] != contraseña.value:
            contraseña.border_color = "red"
            contraseña_error.value = "La contraseña es incorrecta"
        else:
            # Si las credenciales son correctas, obtener todos los datos del usuario
            cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo.value,))
            user_data = cursor.fetchone()

            # Guardar los datos del usuario en la sesión de la página
            page.session.set("usuario", {
                "nombre": user_data[1],         # Nombre del usuario
                "correo": user_data[2],         # Correo del usuario
                "telefono": user_data[4] or ""  # Teléfono del usuario (si existe)
            })
            print("Sesión guardada:", page.session.get("usuario"))

            # Redirigir al menú principal
            go_to_menu()

        # Cerrar conexión y actualizar la vista
        cursor.close()
        conn.close()
        page.update()

    # Título de la vista de login
    titulo = ft.Text("Ingresar", size=30, color="black", weight=ft.FontWeight.BOLD)
    
    # Botón para iniciar sesión
    loguear = ft.FilledButton(text="LOGIN", on_click=validar_login)
    
    # Botón para ir a la vista de registro
    registrar = ft.FilledButton(text="Regístrate", on_click=ir_a_registro)

    # Contenedor con todos los controles de la vista
    contenido = ft.Column(
        [titulo, 
         correo, 
         correo_error, 
         contraseña, 
         contraseña_error, 
         loguear,
         ft.TextButton(
         text="¿Olvidaste la contraseña?",
         style=ft.ButtonStyle(
            color="blue",
            overlay_color="transparent",
            text_style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE)
            ),
            on_click=ir_a_recuperacion
        ),
        registrar],
        alignment=ft.MainAxisAlignment.CENTER,              # Alineación vertical centrada
        horizontal_alignment=ft.CrossAxisAlignment.CENTER   # Alineación horizontal centrada
    )

    # Retornar la vista completa con fondo e interfaz de login encima
    return ft.View(
        route="/",  # Ruta de la vista
        controls=[
            ft.Container(
                width=400,
                height=680,
                content=ft.Stack([  # Se apilan elementos uno sobre otro
                    ft.Image(
                        src="imagenes/fondo.jpg",  # Imagen de fondo
                        fit=ft.ImageFit.COVER,
                        width=400,
                        height=680
                    ),
                    ft.Container(content=contenido, padding=30)  # Contenido encima del fondo
                ])
            )
        ]
    )
