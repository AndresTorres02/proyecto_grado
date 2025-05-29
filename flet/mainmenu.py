import flet as ft

def menu_principal(page: ft.Page):
    # Título
    titulo = ft.Text("Información de usuario", size=20, weight=ft.FontWeight.BOLD, color="black")

    # Fila con ícono e información
    nombre_usuario = ft.Row(
        [
            ft.Image(src="imagenes/label.png", width=25, height=25),
            ft.Text("Nombre del usuario", color="black")
        ],
        spacing=10
    )

    fila_correo = ft.Row(
        [
            ft.Image(src="imagenes/email.png", width=25, height=25),
            ft.Text("correo@ejemplo.com", color="black")
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

    # Columna izquierda con información
    columna_izquierda = ft.Column(
        [titulo, nombre_usuario, fila_correo, fila_telefono],
        spacing=15
    )

    # Imagen a la derecha, con padding superior para centrarla con los textos
    imagen_derecha = ft.Container(
        content=ft.Image(
            src="imagenes/imagen2.png",  # o la imagen que subiste
            width=120,
            height=140,
            fit=ft.ImageFit.CONTAIN
        ),
        padding=ft.padding.only(top=35, left=-35)  # Ajusta este valor según se vea mejor
    )

    registros_fila = ft.Row(
        [
            ft.Text("Registros de mi cultivo", size=18, weight=ft.FontWeight.BOLD, color="black"),
            ft.TextButton("ver todo", style=ft.ButtonStyle(color="blue"))
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    # Fila principal con los dos lados
    fila_contenido = ft.Row(
        [columna_izquierda, imagen_derecha],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.START
    )

    # Fondo
    fondo = ft.Stack([
        ft.Image(
            src="imagenes/fondo.jpg",
            fit=ft.ImageFit.COVER,
            width=400,
            height=800
        ),
        ft.Container(
            content=ft.Column([
                fila_contenido,
                ft.Container(height=25),  # Espaciado
                registros_fila
            ],
            spacing=10
            ),
            padding=20
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
