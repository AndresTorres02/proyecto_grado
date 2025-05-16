import flet as ft

def main(page: ft.Page):

    page.window_width = 400
    page.window_height = 800
    page.window_resizable = False
    page.window_maximizable = False
    page.window_minimizable = False  # Puedes dejar esto en True si quieres permitir minimizar
    page.window_always_on_top = False  # Opcional
    page.update()

    
    def on_submit_correo(e):
        page.controls.append(ft.Text(f"Escribiste: {correo.value}"))
        page.update()

    def on_submit_contraseña(e):
        page.controls.append(ft.Text(f"Escribiste: {contraseña.value}"))
        page.update()

    titulo = ft.Text(
        "Ingresar",
        size=30,
        color=ft.Colors.BLACK,
        weight=ft.FontWeight.BOLD,
    )

    correo = ft.TextField(label="Escribe tu correo", on_submit=on_submit_correo)
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, on_submit=on_submit_contraseña)
    loguear = ft.FilledButton(text="LOGIN")

    olv_contraseña = ft.TextButton(
        "¿Olvidaste la contraseña?",
        style=ft.ButtonStyle(
            padding=0,
            overlay_color="transparent",
            color="blue",
        ),
        url="#"
    )

    registrar = ft.FilledButton(text="Regístrate")

    fila_olv_contraseña = ft.Row(
        [olv_contraseña],
        alignment=ft.MainAxisAlignment.END,
        width=400
    )

    contenido_centrado = ft.Column(
        [
            titulo,
            ft.Container(height=200),  # Espacio entre título y campo de correo
            correo,
            ft.Container(height=20),
            contraseña,
            ft.Container(height=20),
            loguear,
            ft.Container(height=20),
            fila_olv_contraseña,
            ft.Container(height=20),
            registrar
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
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

