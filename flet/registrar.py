import flet as ft
import mysql.connector

# Vista de registro que recibe la página y una función para volver al login
def registrar_view(page: ft.Page, volver_login):

    # Función para volver a la vista de login
    def regresar(e):
        volver_login()


    titulo = ft.Text("Crear cuenta", size=30, color="Black", weight=ft.FontWeight.BOLD)
    correo = ft.TextField(label="Escribe tu correo", label_style=ft.TextStyle(color="Black"))
    nombre = ft.TextField(label="Escribe tu nombre completo", label_style=ft.TextStyle(color="black"))
    telefono = ft.TextField(label="Escribe tu numero de telefono", label_style=ft.TextStyle(color="black"))
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, label_style=ft.TextStyle(color="black"))
    confirmar = ft.TextField(label="Confirmar contraseña", password=True, label_style=ft.TextStyle(color="black"))
    crear = ft.FilledButton(text="CREAR", color="Black")
    volver = ft.FilledButton(text="Volver al Login", color="Black", on_click=regresar)


    # Función para conectarse a la base de datos MySQL
    def conectar_bd():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="q2e4t6@",
            database="sistema_cultivos"
        )

    # Función para cerrar el diálogo de confirmación
    def cerrar_dialogo(e):
        dialog.open = False  # Cierra el diálogo
        page.update()        # Refresca la página
        volver_login()       # Redirige al login

    # Función para limpiar los campos y mensajes de error
    def limpiar_campos():
        for campo in [correo, nombre, contraseña, confirmar]:
            campo.value = ""              # Borra el valor ingresado
            campo.border_color = "grey"   # Restaura el color del borde
        # Limpia los mensajes de ayuda
        correo_helper.value = ""
        nombre_helper.value = ""
        contra_helper.value = ""
        confirmar_helper.value = ""

    # Función que valida y registra al usuario en la base de datos
    def registrar_usuario(e):
        vacio = False  # Indicador de campos vacíos

        # Limpia mensajes de error previos
        correo_helper.value = ""
        nombre_helper.value = ""
        contra_helper.value = ""
        confirmar_helper.value = ""

        # Validación de campos vacíos
        if not correo.value:
            correo.border_color = "red"
            correo_helper.value = "El correo es obligatorio"
            vacio = True
        else:
            correo.border_color = "grey"

        if not nombre.value:
            nombre.border_color = "red"
            nombre_helper.value = "El nombre es obligatorio"
            vacio = True
        else:
            nombre.border_color = "grey"

        if not contraseña.value:
            contraseña.border_color = "red"
            contra_helper.value = "La contraseña es obligatoria"
            vacio = True
        else:
            contraseña.border_color = "grey"

        if not confirmar.value:
            confirmar.border_color = "red"
            confirmar_helper.value = "Debe confirmar la contraseña"
            vacio = True
        else:
            confirmar.border_color = "grey"

        if not pregunta_seguridad.value:
            pregunta_seguridad.border_color = "red"
            vacio = True
        else:
            pregunta_seguridad.border_color = "grey"

        if not respuesta_seguridad.value:
            respuesta_seguridad.border_color = "red"
            vacio = True
        else:
            respuesta_seguridad.border_color = "grey"

        # Si hay algún campo vacío, se detiene la ejecución
        if vacio:
            page.update()
            return

        # Verifica que las contraseñas coincidan
        if contraseña.value != confirmar.value:
            contraseña.border_color = "red"
            confirmar.border_color = "red"
            contra_helper.value = "Las contraseñas no coinciden"
            confirmar_helper.value = "Las contraseñas no coinciden"
            page.update()
            return

        try:
            # Conexión y registro en la base de datos
            conn = conectar_bd()
            cursor = conn.cursor()

            query = "INSERT INTO usuarios (nombre, correo, telefono, contraseña) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (nombre.value, correo.value, telefono.value, contraseña.value))
            conn.commit()
            # Inserta los datos del usuario
            query = "INSERT INTO usuarios (nombre, correo, contraseña, pregunta, info_pregunta) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (
                nombre.value,
                correo.value,
                contraseña.value,
                pregunta_seguridad.value,
                respuesta_seguridad.value.lower()
            ))

            conn.commit()  # Guarda los cambios

            limpiar_campos()  # Limpia los campos luego de registrar

            # Muestra un diálogo de éxito
            dialog.title = ft.Text("Usuario registrado con éxito")
            dialog.open = True
            page.update()

        # Manejo de error si el correo ya existe (clave duplicada)
        except mysql.connector.IntegrityError:
            correo.border_color = "red"
            correo_helper.value = "El correo ya está registrado"
            page.update()

        # Otro error de MySQL, se muestra en la parte inferior
        except mysql.connector.Error as err:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error al registrar: {err}", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()

        # Cierre de conexión y cursor
        finally:
            cursor.close()
            conn.close()

    # Configuración del cuadro de diálogo que se muestra al registrar
    dialog = ft.AlertDialog(
        modal=True,
        actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
        actions_alignment=ft.MainAxisAlignment.END
    )
    page.dialog = dialog  # Asigna el diálogo a la página


    # Campos del formulario y helpers
    titulo = ft.Text("Crear cuenta", size=30, color="white", weight=ft.FontWeight.BOLD)

    # Campo de correo y mensaje de error
    correo_helper = ft.Text("", size=12, color="red")
    correo = ft.TextField(label="Escribe tu correo", color="black", label_style=ft.TextStyle(color="black"), border_color="grey")

    # Campo de nombre y mensaje de error
    nombre_helper = ft.Text("", size=12, color="red")
    nombre = ft.TextField(label="Escribe tu nombre completo", color="black", label_style=ft.TextStyle(color="black"), border_color="grey")

    # Preguntas de seguridad (Dropdown)
    pregunta_seguridad = ft.Dropdown(
        label="Selecciona una pregunta de seguridad",
        options=[
            ft.dropdown.Option("¿Cuál es el nombre de tu primera mascota?"),
            ft.dropdown.Option("¿En qué ciudad naciste?"),
            ft.dropdown.Option("¿Cuál es tu comida favorita?"),
            ft.dropdown.Option("¿Cuál es el segundo nombre de tu madre?"),
            ft.dropdown.Option("¿Cuál fue el nombre de tu primera escuela?")
        ],
        border_color="grey"
    )

    # Campo para responder la pregunta
    respuesta_seguridad = ft.TextField(
        label="Escribe tu respuesta",
        color="black",
        label_style=ft.TextStyle(color="black"),
        border_color="grey"
    )

    # Campo de contraseña y mensaje de error
    contra_helper = ft.Text("", size=12, color="red")
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, color="black", label_style=ft.TextStyle(color="black"), border_color="grey")

    # Campo para confirmar contraseña y mensaje de error
    confirmar_helper = ft.Text("", size=12, color="red")
    confirmar = ft.TextField(label="Confirmar contraseña", password=True, color="black", label_style=ft.TextStyle(color="black"), border_color="grey")


    titulo = ft.Text("Crear cuenta", size=30, color="Black", weight=ft.FontWeight.BOLD)
    correo = ft.TextField(label="Escribe tu correo", color="black", label_style=ft.TextStyle(color="black"))
    nombre = ft.TextField(label="Escribe tu nombre completo", color="black", label_style=ft.TextStyle(color="black"))
    telefono = ft.TextField(label="Escribe tu numero de telefono", color="black", label_style=ft.TextStyle(color="black"))
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, color="black", label_style=ft.TextStyle(color="black"))
    confirmar = ft.TextField(label="Confirmar contraseña", password=True, color="black", label_style=ft.TextStyle(color="black"))

    # Botones del formulario
    crear = ft.FilledButton(text="CREAR", on_click=registrar_usuario)
    volver = ft.FilledButton(text="Volver al Login", on_click=regresar)

    # Organización de los controles en una columna central
    contenido = ft.Column(

        [
            titulo,
            correo,
            correo_helper,
            nombre,
            nombre_helper,
            contraseña,
            contra_helper,
            confirmar,
            confirmar_helper,
            pregunta_seguridad,
            respuesta_seguridad,
            crear,
            volver
        ],

        [titulo, correo, nombre, telefono, contraseña, confirmar, crear, volver],

        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO
    )

    # Retorna la vista completa con fondo y formulario
    return ft.View(
        route="/registrar",
        controls=[
            ft.Stack([
                # Imagen de fondo
                ft.Image(
                    src="imagenes/fondo.jpg",
                    fit=ft.ImageFit.COVER,
                    width=400,
                    height=800
                ),
                # Contenedor del formulario
                ft.Container(content=contenido, padding=30),
                # Diálogo de confirmación
                dialog
            ])
        ]
    )
