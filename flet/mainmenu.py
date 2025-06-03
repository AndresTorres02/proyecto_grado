import flet as ft

def menu_principal(page: ft.Page, go_to_info):

    def ir_a_info_detallada(e):
        go_to_info()

    def cerrar_sesion(e):
        page.session.clear()
        page.snack_bar = ft.SnackBar(ft.Text("Sesión cerrada con éxito"))
        page.snack_bar.open = True
        page.update()
        page.go("/")

    # Datos del usuario
    usuario = page.session.get("usuario") or {
        "nombre": "andres torres",
        "correo": "aftm@gmail.com",
        "telefono": "+57 123 456 7890"
    }

    # TextFields ocultos al inicio
    nombre_field = ft.TextField(value=usuario["nombre"], color="black", visible=False)
    correo_field = ft.TextField(value=usuario["correo"], color="black", visible=False)
    telefono_field = ft.TextField(value=usuario["telefono"], color="black", visible=False)

    nombre_text = ft.Text(usuario["nombre"], color="black")
    correo_text = ft.Text(usuario["correo"], color="black")
    telefono_text = ft.Text(usuario["telefono"], color="black")

    # Estados
    estado = {"nombre": False, "correo": False, "telefono": False}

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

    boton_nombre = ft.Image(
        src="imagenes/pen.png", 
        width=25,
        height=25
    )
    boton_nombre.on_click = toggle_edicion("nombre")

    boton_correo = ft.Image(
        src="imagenes/pen.png",
        width=25,
        height=25
    )
    boton_correo.on_click = toggle_edicion("correo")

    boton_telefono = ft.Image(
        src="imagenes/pen.png",
        width=25,
        height=25
    )
    boton_telefono.on_click = toggle_edicion("telefono")

    # Fila nombre
    fila_nombre = ft.Row(
        [
            ft.Image(src="imagenes/label.png", width=25, height=25),
            nombre_text,
            nombre_field,
            boton_nombre
        ],
        spacing=10
    )

    # Fila correo
    fila_correo = ft.Row(
        [
            ft.Image(src="imagenes/email.png", width=25, height=25),
            correo_text,
            correo_field,
            boton_correo
        ],
        spacing=10
    )

    # Fila teléfono
    fila_telefono = ft.Row(
        [
            ft.Image(src="imagenes/telephone.png", width=25, height=25),
            telefono_text,
            telefono_field,
            boton_telefono
        ],
        spacing=10
    )

    # Imagen que actúa como botón de guardar
    boton_guardar = ft.Image(
        src="imagenes/diskette.png",
        width=35,
        height=35
    )
    boton_guardar.on_click = guardar_cambios

    columna_izquierda = ft.Column(
        [
            ft.Text("Información de usuario", size=20, weight=ft.FontWeight.BOLD, color="black"),
            fila_nombre,
            fila_correo,
            fila_telefono,
            boton_guardar
        ],
        spacing=15
    )

    imagen_derecha = ft.Container(
        content=ft.Image(
            src="imagenes/imagen2.png",
            width=120,
            height=140,
            fit=ft.ImageFit.CONTAIN
        ),
        padding=ft.padding.only(top=35, left=-35)
    )

    registros_fila = ft.Row(
        [
            ft.Text("Registros de mi cultivo", size=18, weight=ft.FontWeight.BOLD, color="black"),
            ft.TextButton("Ver todo", style=ft.ButtonStyle(color="blue"), on_click=ir_a_info_detallada)
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    fila_contenido = ft.Row(
        [columna_izquierda, imagen_derecha],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.START
    )

    boton_cerrar_sesion = ft.Row(
        [
            ft.Image(src="imagenes/salida.png", width=25, height=25),
            ft.TextButton("Cerrar sesión", on_click=cerrar_sesion, style=ft.ButtonStyle(color="red"))
        ],
        spacing=10,
        alignment=ft.MainAxisAlignment.START
    )

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
        )
    ])

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
