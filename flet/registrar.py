import flet as ft

def registrar_view(page: ft.Page, volver_login):
    def regresar(e):
        volver_login()

    titulo = ft.Text("Crear cuenta", size=30, color="Black", weight=ft.FontWeight.BOLD)
    correo = ft.TextField(label="Escribe tu correo", label_style=ft.TextStyle(color="Black"))
    nombre = ft.TextField(label="Escribe tu nombre completo", label_style=ft.TextStyle(color="black"))
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, label_style=ft.TextStyle(color="black"))
    confirmar = ft.TextField(label="Confirmar contraseña", password=True, label_style=ft.TextStyle(color="black"))
    crear = ft.FilledButton(text="CREAR", color="Black")
    volver = ft.FilledButton(text="Volver al Login", color="Black", on_click=regresar)

    contenido = ft.Column(
        [titulo, correo, nombre, contraseña, confirmar, crear, volver],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO
    )

    return ft.View(
        route="/registrar",
        controls=[
            ft.Stack([
                ft.Image(
                    src="imagenes/fondo.jpg",
                    fit=ft.ImageFit.COVER,
                    width=400,
                    height=800
                ),
                ft.Container(
                    content=contenido,
                    padding=30
                )
            ])
        ]
    )