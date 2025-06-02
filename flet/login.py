import flet as ft
import mysql.connector

def login_view(page: ft.Page, go_to_registrar, go_to_menu):

    def conectar_bd():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="a1b2c3d4_",
            database="sistema_cultivos"
    )

    def validar_login(e):
        conn = conectar_bd()
        cursor = conn.cursor()

        query = "SELECT * FROM usuarios WHERE correo = %s AND contraseña = %s"
        cursor.execute(query, (correo.value, contraseña.value))
        resultado = cursor.fetchone()

        if resultado:
            # Puedes mostrar un mensaje de bienvenida opcional
            page.snack_bar = ft.SnackBar(
                ft.Text("¡Bienvenido!", color="white"),
                bgcolor="green"
            )
            page.snack_bar.open = True
            page.update()

            # Redirigir directamente
            go_to_menu()
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("Correo o contraseña incorrectos", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()

        cursor.close()
        conn.close()


    titulo = ft.Text("Ingresar", size=30, color="black", weight=ft.FontWeight.BOLD)
    correo = ft.TextField(label="Escribe tu correo", text_style=ft.TextStyle(color="black"), border_color="black")
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, text_style=ft.TextStyle(color="black"), border_color="black")
    loguear = ft.FilledButton(text="LOGIN", on_click=validar_login)
    registrar = ft.FilledButton(text="Regístrate", on_click=lambda e: go_to_registrar())

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

