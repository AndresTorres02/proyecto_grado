import flet as ft
from abrircamara import abrir_camara


def menu_principal(page: ft.Page, go_to_info, go_to_crud, go_to_abrir_camara):

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

    # Recupera información del usuario desde la sesión
    usuario = page.session.get("usuario")  # sin valores por defecto

    # Campos ocultos para edición
    nombre_field = ft.TextField(value=usuario["nombre"], color="black", visible=False)
    correo_field = ft.TextField(value=usuario["correo"], color="black", visible=False)
    telefono_field = ft.TextField(value=usuario["telefono"], color="black", visible=False)

    # Textos visibles
    nombre_text = ft.Text(usuario["nombre"], color="black")
    correo_text = ft.Text(usuario["correo"], color="black")
    telefono_text = ft.Text(usuario["telefono"], color="black")

    # Diccionario de estado de edición
    estado = {"nombre": False, "correo": False, "telefono": False}

    # Alternar entre texto y campo editable
    def toggle_edicion(campo):
        def handler(e):
            estado[campo] = not estado[campo]

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

            page.update()
        return handler

    # Guardar cambios
    def guardar_cambios(e):
        usuario["nombre"] = nombre_field.value
        usuario["correo"] = correo_field.value
        usuario["telefono"] = telefono_field.value

        nombre_text.value = usuario["nombre"]
        correo_text.value = usuario["correo"]
        telefono_text.value = usuario["telefono"]

        page.session.set("usuario", usuario)

        page.snack_bar = ft.SnackBar(ft.Text("Información actualizada"))
        page.snack_bar.open = True
        page.update()

    # Botones de edición
    boton_nombre = ft.Image(src="imagenes/pen.png", width=25, height=25)
    boton_nombre.on_click = toggle_edicion("nombre")

    boton_correo = ft.Image(src="imagenes/pen.png", width=25, height=25)
    boton_correo.on_click = toggle_edicion("correo")

    boton_telefono = ft.Image(src="imagenes/pen.png", width=25, height=25)
    boton_telefono.on_click = toggle_edicion("telefono")

    # Filas con íconos e información
    fila_nombre = ft.Row(
        [
            ft.Image(src="imagenes/label.png", width=25, height=25),
            nombre_text
        ],
        spacing=10
    )

    fila_correo = ft.Row(
        [
            ft.Image(src="imagenes/email.png", width=25, height=25),
            correo_text,
        ],
        spacing=10
    )

    fila_telefono = ft.Row(
        [
            ft.Image(src="imagenes/telephone.png", width=25, height=25),
            telefono_text,
        ],
        spacing=10
    )

    # Botón para guardar cambios (icono disquete)
    boton_guardar = ft.Image(
        src="imagenes/diskette.png",
        width=35,
        height=35
    )
    boton_guardar.on_click = guardar_cambios

    # Botón para ir al CRUD
    boton_ir_a_crud = ft.ElevatedButton(
        "editar info",
        on_click=go_to_crud,
        icon=ft.Icons.EDIT
    )

    # Columna izquierda con la info del usuario
    columna_izquierda = ft.Column(
        [
            ft.Text("Información de usuario", size=20, weight=ft.FontWeight.BOLD, color="black"),
            fila_nombre,
            fila_correo,
            fila_telefono,
            boton_ir_a_crud,
        ],
        spacing=15
    )

    # Imagen decorativa lateral
    imagen_derecha = ft.Container(
        content=ft.Image(
            src="imagenes/imagen2.png",
            width=120,
            height=140,
            fit=ft.ImageFit.CONTAIN
        ),
        padding=ft.padding.only(top=35, left=-35)
    )

    # Fila superior con registros y botón "ver todo"
    registros_fila = ft.Row(
        [
            ft.Text("Registros de mi cultivo", size=18, weight=ft.FontWeight.BOLD, color="black"),
            ft.TextButton("Ver todo", style=ft.ButtonStyle(color="blue"), on_click=ir_a_info_detallada)
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Fila que combina columna de datos con imagen decorativa
    fila_contenido = ft.Row(
        [columna_izquierda, imagen_derecha],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.START
    )

    # Botón de cerrar sesión
    boton_cerrar_sesion = ft.Row(
        [
            ft.Image(src="imagenes/salida.png", width=25, height=25),
            ft.TextButton("Cerrar sesión", on_click=cerrar_sesion, style=ft.ButtonStyle(color="red"))
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.START
    )

    #boton cámara
    boton_camara = ft.Container(
        alignment=ft.alignment.bottom_center,
        margin=ft.margin.only(bottom=20),
        content=ft.IconButton(
            on_click=go_to_abrir_camara,  # Usa la función pasada desde main
            icon=None,
            icon_size=0,
            style=ft.ButtonStyle(
                padding=0,
                shape=ft.RoundedRectangleBorder(radius=15),
            ),
            content=ft.Image(
                src="imagenes/camara.png",
                width=120,
                height=120,
                fit=ft.ImageFit.CONTAIN
            )
        )
    )

    # Fondo con imagen, contenido principal, botón de cerrar sesión y botón de cámara
    fondo = ft.Stack([
        ft.Image(
            src="imagenes/fondo.jpg",
            fit=ft.ImageFit.COVER,
            width=400,
            height=800
        ),
        ft.Container(
            content=ft.Column(
                [
                    fila_contenido,
                    ft.Container(height=25),
                    registros_fila
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=20
        ),
        ft.Container(
            content=boton_cerrar_sesion,
            left=20,
            bottom=60
        ),
        boton_camara  #se incluye en la pila de elementos visibles
    ])

    # Devuelve la vista principal
    return ft.View(
        route="/menu",
        controls=[
            ft.Container(
                width=400,
                height=800,
                content=fondo
            )
        ]
    )
