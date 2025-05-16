import flet as ft

def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 800
    page.window_resizable = False

    def on_submit_correo(e):
        page.controls.append(ft.Text(f"Escribiste: {correo.value}"))
        page.update()

    def on_submit_nombre(e):
        page.controls.append(ft.Text(f"Escribiste: {nombre.value}"))
        page.update()

    def on_submit_contraseña(e):
        page.controls.append(ft.Text(f"Escribiste: {contraseña.value}"))
        page.update()

    def on_submit_confirmarcontraseña(e):
        page.controls.append(ft.Text(f"Escribiste: {confirmarcontraseña.value}"))
        page.update()

    titulo = ft.Text(
        "Crear cuenta",
        size=30,
        color=ft.Colors.WHITE,  # Blanco para que resalte sobre fondo
        weight=ft.FontWeight.BOLD,
    )

    correo = ft.TextField(label="Escribe tu correo", on_submit=on_submit_correo)
    nombre = ft.TextField(label="Escribe tu nombre completo", on_submit=on_submit_nombre)
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, on_submit=on_submit_contraseña)
    confirmarcontraseña = ft.TextField(label="Confirmar contraseña", password=True, on_submit=on_submit_confirmarcontraseña)
    crear = ft.FilledButton(text="CREAR")
    registrar = ft.FilledButton(text="Regístrate")

    contenido_centrado = ft.Column(
        [
            titulo,
            ft.Container(height=40),
            correo,
            ft.Container(height=20),
            nombre,
            ft.Container(height=20),
            contraseña,
            ft.Container(height=20),
            confirmarcontraseña,
            ft.Container(height=20),
            crear,
            ft.Container(height=20),
            registrar
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    stack = ft.Stack(
        [
            ft.Image(
                src="C:/Users/FELIPE/Desktop/Uceva/Semestre X/Proyecto/imagenes/fondo.jpg",
                fit=ft.ImageFit.COVER,
                width=400,
                height=800
            ),
            ft.Container(
                content=contenido_centrado,
                padding=30
            )
        ],
        expand=True
    )

    page.add(stack)

ft.app(target=main)
