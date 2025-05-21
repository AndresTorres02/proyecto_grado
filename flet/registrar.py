import flet as ft

def registrar_view(page: ft.Page, volver_login):
    def regresar(e):
        volver_login()

    titulo = ft.Text("Crear cuenta", size=30, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)
    correo = ft.TextField(label="Escribe tu correo")
    nombre = ft.TextField(label="Escribe tu nombre completo")
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True)
    confirmar = ft.TextField(label="Confirmar contraseña", password=True)
    crear = ft.FilledButton(text="CREAR")
    volver = ft.FilledButton(text="Volver al Login", on_click=regresar)

    contenido = ft.Column(
        [titulo, correo, nombre, contraseña, confirmar, crear, volver],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    return ft.View(
        route="/registrar",
        controls=[
            ft.Stack([
                ft.Image(
                    src="C:/Users/FELIPE/Desktop/Uceva/Semestre X/Proyecto/imagenes/fondo.jpg",
                    fit=ft.ImageFit.COVER,
                    expand=True
                ),
                ft.Container(
                    content=contenido,
                    padding=30
                )
            ])
        ]
    )