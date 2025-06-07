import flet as ft
from conexion import get_user_by_email, update_user # Importa las funciones desde tu 'conexion.py'

def crud_user(page: ft.Page, volver_al_menu):

    # --- 1. Obtener datos del usuario de la sesión, luego cargar los datos actuales desde la BD ---
    # La sesión debe contener principalmente el correo electrónico (o ID) del usuario para buscar sus datos completos.
    usuario_sesion = page.session.get("usuario")

    # Si no hay usuario en la sesión o le falta el correo electrónico, redirige al login (o maneja como un error)
    if not usuario_sesion or "correo" not in usuario_sesion:
        print("Error: No se encontró un usuario en la sesión o falta el correo electrónico. Redirigiendo al login.")
        page.go("/") # Redirige a la página de login
        return ft.View(route="/") # Retorna una vista vacía para evitar errores adicionales

    # Carga los datos más recientes del usuario desde la base de datos utilizando el correo de la sesión
    usuario_db = get_user_by_email(usuario_sesion["correo"])

    # Usa los datos de la BD si se encuentran; de lo contrario, usa los datos de la sesión (y muestra una advertencia)
    if usuario_db:
        usuario_actual = usuario_db
    else:
        usuario_actual = usuario_sesion # Si la búsqueda en la BD falla, se usa la información de la sesión como respaldo
        page.snack_bar = ft.SnackBar(ft.Text("Advertencia: Datos de usuario no encontrados en la BD. Usando datos de sesión."))
        page.snack_bar.open = True
        page.update()

    # --- 2. Campos de texto para editar ---
    # Rellena los campos con los datos de 'usuario_actual' (que provienen de la BD o de la sesión)
    nombre_field = ft.TextField(label="Nombre", value=usuario_actual.get("nombre", ""), width=300, color="black")
    # El campo de correo se hace de solo lectura ya que suele ser el identificador único
    correo_field = ft.TextField(label="Correo", value=usuario_actual.get("correo", ""), width=300, color="black", read_only=True)
    telefono_field = ft.TextField(label="Número telefónico", value=usuario_actual.get("telefono", ""), width=300, color="black")
    # Para la contraseña, el 'value' debe estar vacío; el usuario ingresa una *nueva* contraseña si desea cambiarla.
    contrasena_field = ft.TextField(label="Nueva Contraseña (dejar vacío para no cambiar)", value="", password=True, can_reveal_password=True, width=300, color="black")

    # --- 3. Acción de guardar ---
    def guardar_cambios(e):
        current_email = usuario_actual["correo"] # Usa el correo electrónico del usuario cargado

        # Prepara los datos a enviar a la base de datos. Solo incluye los campos que pueden ser cambiados.
        datos_a_actualizar_bd = {
            "nombre": nombre_field.value,
            "telefono": telefono_field.value
        }

        # Agrega condicionalmente la contraseña a los datos de actualización solo si el usuario ha escrito algo
        if contrasena_field.value:
            datos_a_actualizar_bd["contrasena"] = contrasena_field.value

        # --- Llama a la función de actualización de la base de datos ---
        if update_user(current_email, datos_a_actualizar_bd):
            # Si la actualización en la BD es exitosa, también actualiza la sesión de Flet
            # Es crucial asegurarse de que la sesión refleje la contraseña real (la nueva o la antigua)
            usuario_actualizado_en_sesion = usuario_actual.copy() # Inicia con los datos actuales del usuario (de la BD/sesión)
            usuario_actualizado_en_sesion.update(datos_a_actualizar_bd) # Aplica los campos actualizados

            # Si el campo de contraseña estaba vacío, la clave 'contrasena' podría no estar en datos_a_actualizar_bd.
            # Queremos que la sesión mantenga la contraseña antigua en este caso.
            if not contrasena_field.value and "contrasena" not in datos_a_actualizar_bd:
                usuario_actualizado_en_sesion["contrasena"] = usuario_actual.get("contrasena", "")

            page.session.set("usuario", usuario_actualizado_en_sesion)
            page.snack_bar = ft.SnackBar(ft.Text("Información actualizada con éxito en la BD."))
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al actualizar información en la BD."))

        page.snack_bar.open = True
        page.update()

    # --- 4. Acción de volver ---
    def volver(e):
        volver_al_menu(e)

    # --- 5. Diseño del contenido ---
    contenido = ft.Column(
        [
            ft.Text("Editar información de usuario", size=22, weight=ft.FontWeight.BOLD, color="black"),
            nombre_field,
            correo_field,
            telefono_field,
            contrasena_field,
            ft.Row(
                [
                    ft.ElevatedButton("Guardar", on_click=guardar_cambios),
                    ft.ElevatedButton("Volver", on_click=volver)
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    # --- 6. Imagen de fondo ---
    # Usa page.window.width/height para una mejor adaptabilidad si la ventana es redimensionable
    fondo = ft.Image(
        src="imagenes/fondo.jpg", # Asegúrate de que esta ruta sea correcta
        fit=ft.ImageFit.COVER,
        width=page.window.width, # Usa las dimensiones de la ventana
        height=page.window.height # Usa las dimensiones de la ventana
    )

    # --- 7. Retorna la vista de Flet ---
    return ft.View(
        route="/editar_usuario",
        controls=[
            ft.Stack(
                [
                    fondo, # Imagen de fondo como primera capa
                    ft.Container(
                        content=contenido,
                        width=page.window.width, # Ajusta el contenedor al tamaño de la ventana
                        height=page.window.height, # Ajusta el contenedor al tamaño de la ventana
                        alignment=ft.alignment.center # Centra el contenido
                    )
                ],
                width=page.window.width, # El Stack mismo debe coincidir con el tamaño de la ventana
                height=page.window.height
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.MainAxisAlignment.CENTER
    )