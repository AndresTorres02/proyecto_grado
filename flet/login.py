import flet as ft

def login_view(page: ft.Page, go_to_registrar):
    def ir_a_registro(e):
        go_to_registrar()

    titulo = ft.Text("Ingresar", size=30, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD)
    correo = ft.TextField(
        label="Escribe tu correo",
        text_style=ft.TextStyle(color="black"),
        border_color="black"
    )
    contraseña = ft.TextField(
        label="Escribe tu contraseña",
        password=True,
        text_style=ft.TextStyle(color="black"),
        border_color="black"
    )
    loguear = ft.FilledButton(text="LOGIN")
    registrar = ft.FilledButton(text="Regístrate", on_click=ir_a_registro)

    contenido = ft.Column(
        [titulo, correo, contraseña, loguear, registrar],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    return ft.View(
        route="/",
        controls=[
            ft.Stack([
                ft.Image(
                    src="C:/Users/FELIPE/Desktop/Uceva/Semestre X/Proyecto/imagenes/fondo.jpg",
                    fit=ft.ImageFit.COVER,
                    width=400,
                    height=800
                ),
                ft.Container(content=contenido, padding=30)
            ])
        ]
    )
