# Importamos la biblioteca Flet
import flet as ft

def menu_principal(page: ft.Page, go_to_info, debug_go_to_crud):


    # Función para navegar a la pantalla de información detallada
    def ir_a_info_detallada(e):
        go_to_info()

    # Función para cerrar sesión del usuario
    def cerrar_sesion(e):
        page.session.clear()  # Limpia los datos de sesión
        page.snack_bar = ft.SnackBar(ft.Text("Sesión cerrada con éxito"))  # Muestra notificación
        page.snack_bar.open = True
        page.update()
        page.go("/")  # Redirige al inicio


    # Recupera la información del usuario desde la sesión, o usa valores por defecto si no existe
    usuario = page.session.get("usuario") or {
        "nombre": "andres torres",
        "correo": "aftm@gmail.com",
        "telefono": "+57 123 456 7890"
    }

    # Campos ocultos para editar la información del usuario
    nombre_field = ft.TextField(value=usuario["nombre"], color="black", visible=False)
    correo_field = ft.TextField(value=usuario["correo"], color="black", visible=False)
    telefono_field = ft.TextField(value=usuario["telefono"], color="black", visible=False)

    # Datos del usuario
    usuario = page.session.get("usuario") ## le he quitado el or 


    # Textos visibles para mostrar la información del usuario
    nombre_text = ft.Text(usuario["nombre"], color="black")
    correo_text = ft.Text(usuario["correo"], color="black")
    telefono_text = ft.Text(usuario["telefono"], color="black")


    # Diccionario que guarda el estado de edición de cada campo
    estado = {"nombre": False, "correo": False, "telefono": False}

    # Función que permite alternar entre mostrar texto o campo editable
    def toggle_edicion(campo):
        def handler(e):
            estado[campo] = not estado[campo]  # Cambia el estado del campo

            # Alterna visibilidad y cambia el ícono del botón según el estado
            if campo == "nombre":
                nombre_field.visible = estado[campo]
                nombre_text.visible = not estado[campo]
                boton_nombre.icon = ft.icons.SAVE if estado[campo] else ft.icons.EDIT
            elif campo == "correo":
                correo_field.visible = estado[campo]
                correo_text.visible = not estado[campo]
                boton_correo.icon = ft.icons.SAVE if estado[campo] else ft.icons.EDIT
            elif campo == "telefono":
                telefono_field.visible = estado[campo]
                telefono_text.visible = not estado[campo]
                boton_telefono.icon = ft.icons.SAVE if estado[campo] else ft.icons.EDIT

            page.update()  # Refresca la interfaz
        return handler

    # Función para guardar los cambios realizados en los campos editables
    def guardar_cambios(e):
        # Actualiza el diccionario del usuario con los nuevos valores
        usuario["nombre"] = nombre_field.value
        usuario["correo"] = correo_field.value
        usuario["telefono"] = telefono_field.value

        # Actualiza los textos visibles con los nuevos valores
        nombre_text.value = usuario["nombre"]
        correo_text.value = usuario["correo"]
        telefono_text.value = usuario["telefono"]

        # Guarda los cambios en la sesión
        page.session.set("usuario", usuario)

        # Muestra una notificación de éxito
        page.snack_bar = ft.SnackBar(ft.Text("Información actualizada"))
        page.snack_bar.open = True
        page.update()

    # Botones (íconos de lápiz) para editar nombre, correo y teléfono
    boton_nombre = ft.Image(src="imagenes/pen.png", width=25, height=25)
    boton_nombre.on_click = toggle_edicion("nombre")

    boton_correo = ft.Image(src="imagenes/pen.png", width=25, height=25)
    boton_correo.on_click = toggle_edicion("correo")

    boton_telefono = ft.Image(src="imagenes/pen.png", width=25, height=25)
    boton_telefono.on_click = toggle_edicion("telefono")


    # Fila nombre (se modifica para un boton de edicion)


    # Fila para mostrar/editar el nombre

    fila_nombre = ft.Row(
        [
            ft.Image(src="imagenes/label.png", width=25, height=25),
            nombre_text
        ],
        spacing=10
    )

    # Fila para mostrar/editar el correo
    fila_correo = ft.Row(
        [
            ft.Image(src="imagenes/email.png", width=25, height=25),
            correo_text,
            ],
        spacing=10
    )

    # Fila para mostrar/editar el teléfono
    fila_telefono = ft.Row(
        [
            ft.Image(src="imagenes/telephone.png", width=25, height=25),
            telefono_text,
        ],
        spacing=10
    )

    boton_guardar = ft.Image(
        src="imagenes/diskette.png",
        width=35,
        height=35
        )

    boton_ir_a_crud = ft.ElevatedButton(
        "editar info",
        on_click=debug_go_to_crud,
        icon=ft.Icons.EDIT

    )
    # Botón para guardar cambios (ícono de disquete)
    boton_guardar = ft.Image(src="imagenes/diskette.png", width=35, height=35)
    boton_guardar.on_click = guardar_cambios

    # Columna con toda la información del usuario y el botón de guardar
    columna_izquierda = ft.Column(
        [
            ft.Text("Información de usuario", size=20, weight=ft.FontWeight.BOLD, color="black"),
            fila_nombre,
            fila_correo,
            fila_telefono,
            boton_ir_a_crud
        ],
        spacing=15
    )

    # Imagen decorativa a la derecha del contenido
    imagen_derecha = ft.Container(
        content=ft.Image(
            src="imagenes/imagen2.png",
            width=120,
            height=140,
            fit=ft.ImageFit.CONTAIN
        ),
        padding=ft.padding.only(top=35, left=-35)
    )

    # Fila para mostrar título y botón de navegación a registros
    registros_fila = ft.Row(
        [
            ft.Text("Registros de mi cultivo", size=18, weight=ft.FontWeight.BOLD, color="black"),
            ft.TextButton("Ver todo", style=ft.ButtonStyle(color="blue"), on_click=ir_a_info_detallada)
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Fila principal que contiene la columna izquierda y la imagen derecha
    fila_contenido = ft.Row(
        [columna_izquierda, imagen_derecha],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.START
    )

    # Botón para cerrar sesión del usuario
    boton_cerrar_sesion = ft.Row(
        [
            ft.Image(src="imagenes/salida.png", width=25, height=25),
            ft.TextButton("Cerrar sesión", on_click=cerrar_sesion, style=ft.ButtonStyle(color="red"))
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.START
    )

    # Fondo principal de la vista con imagen de fondo, contenido y botón de cerrar sesión
    fondo = ft.Stack([
        ft.Image(
            src="imagenes/fondo.jpg",
            fit=ft.ImageFit.COVER,
            width=400,
            height=680
        ),
        ft.Container(
            width=400,
            height=680,
            content=ft.Column(
                [
                    fila_contenido,
                    ft.Container(height=25),
                    registros_fila,
                    ft.Container(height=30),
                    boton_cerrar_sesion
                ],
                scroll=ft.ScrollMode.AUTO,  # Habilita scroll si el contenido excede
            ),
            padding=20,
            alignment=ft.alignment.top_left,
        )
    ])


    # Devuelve la vista completa del menú principal
    return ft.View(
        route="/menu",
        controls=[
            ft.Container(
                width=400,
                height=680,
                content=fondo
            )
        ],
        #scroll=ft.ScrollMode.AUTO
    )
