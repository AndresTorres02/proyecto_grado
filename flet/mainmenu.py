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

    usuario = page.session.get("usuario") or {"nombre": "Desconocido", "correo": "N/A"}

    titulo = ft.Text("Información de usuario", size=20, weight=ft.FontWeight.BOLD, color="black")

    nombre_usuario = ft.Row(
        [
            ft.Image(src="imagenes/label.png", width=25, height=25),
            ft.Text(usuario["nombre"], color="black")
        ],
        spacing=10
    )

    fila_correo = ft.Row(
        [
            ft.Image(src="imagenes/email.png", width=25, height=25),
            ft.Text(usuario["correo"], color="black")
        ],
        spacing=10
    )

    fila_telefono = ft.Row(
        [
            ft.Image(src="imagenes/telephone.png", width=25, height=25),
            ft.Text("+57 123 456 7890", color="black")
        ],
        spacing=10
    )

    columna_izquierda = ft.Column(
        [titulo, nombre_usuario, fila_correo, fila_telefono],
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
            ft.TextButton("Ver todo", style=ft.ButtonStyle(color="blue"),on_click=ir_a_info_detallada)
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
            ft.Image(src="imagenes/logout.png", width=25, height=25),
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
                    registros_fila,
                    ft.Container(height=30), 
                ],
                spacing=10,
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            ),
            padding=20
        ),
        ft.Container(
        content=boton_cerrar_sesion,
        left=20,
        bottom=60,
        )
    ])

    def cerrar_sesion(e):
        page.session.clear()
        page.go("/")  # Redirige al login

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
