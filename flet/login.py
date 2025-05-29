import flet as ft

def login_view(page: ft.Page, go_to_registrar, go_to_menu):
    def ir_a_registro(e):
        go_to_registrar()

    def ir_a_menu(e):
        go_to_menu()

    titulo = ft.Text("Ingresar", size=30, color="black" , weight=ft.FontWeight.BOLD)
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
    loguear = ft.FilledButton(text="LOGIN", on_click=ir_a_menu)
    registrar = ft.FilledButton(text="Regístrate", on_click=ir_a_registro)

    contenido = ft.Column(
        [titulo, correo, contraseña, loguear, registrar],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    return ft.View(
    route="/",
    controls=[
        ft.Container(
            width=400,
            height=800,
            content=ft.Stack([
                ft.Image(
                    src="imagenes/fondo.jpg",
                    fit=ft.ImageFit.COVER,
                    width=400,
                    height=800
                ),
                ft.Container(content=contenido, padding=30)
            ])
        )
    ]
)

