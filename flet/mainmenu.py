import flet as ft

def menu_principal(page: ft.Page, go_to_info, debug_go_to_crud):

    def ir_a_info_detallada(e):
        go_to_info()

    def cerrar_sesion(e):
        page.session.clear()
        page.snack_bar = ft.SnackBar(ft.Text("Sesión cerrada con éxito"))
        page.snack_bar.open = True
        page.update()
        page.go("/")

    # Datos del usuario
    usuario = page.session.get("usuario") ## le he quitado el or 

    nombre_text = ft.Text(usuario["nombre"], color="black")
    correo_text = ft.Text(usuario["correo"], color="black")
    telefono_text = ft.Text(usuario["telefono"], color="black")

    # Fila nombre (se modifica para un boton de edicion)
    fila_nombre = ft.Row(
        [
            ft.Image(src="imagenes/label.png", width=25, height=25),
            nombre_text
        ],
        spacing=10
    )

    # Fila correo
    fila_correo = ft.Row(
        [
            ft.Image(src="imagenes/email.png", width=25, height=25),
            correo_text,
            ],
        spacing=10
    )

    # Fila teléfono
    fila_telefono = ft.Row(
        [
            ft.Image(src="imagenes/telephone.png", width=25, height=25),
            telefono_text,
        ],
        spacing=10
    )

    boton_ir_a_crud = ft.ElevatedButton(
        "editar info",
        on_click=debug_go_to_crud,
        icon=ft.Icons.EDIT
    )

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
