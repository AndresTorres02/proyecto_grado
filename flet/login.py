import flet as ft
import mysql.connector

def login_view(page: ft.Page, go_to_registrar, go_to_menu):
    def ir_a_registro(e):
        go_to_registrar()

    def conectar_bd():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="q2e4t6@", #cambie la contraseña del conector para que me sirviera
            database="sistema_cultivos"
        )

    correo = ft.TextField(label="Escribe tu correo", text_style=ft.TextStyle(color="black"), border_color="black")
    correo_error = ft.Text("", color="red", size=12)

    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, text_style=ft.TextStyle(color="black"), border_color="black")
    contraseña_error = ft.Text("", color="red", size=12)

    dialog = ft.AlertDialog()

    def validar_login(e):
        # Limpiar errores previos
        correo.border_color = "black"
        contraseña.border_color = "black"
        correo_error.value = ""
        contraseña_error.value = ""

        campos_vacios = False
        if not correo.value.strip():
            correo.border_color = "red"
            correo_error.value = "Este campo es obligatorio"
            campos_vacios = True

        if not contraseña.value.strip():
            contraseña.border_color = "red"
            contraseña_error.value = "Este campo es obligatorio"
            campos_vacios = True

        if campos_vacios:
            page.update()
            return

        conn = conectar_bd()
        cursor = conn.cursor()

        cursor.execute("SELECT contraseña FROM usuarios WHERE correo = %s", (correo.value,))
        result = cursor.fetchone()

        if result is None:
            correo.border_color = "red"
            correo_error.value = "El correo no está registrado"
        elif result[0] != contraseña.value:
            contraseña.border_color = "red"
            contraseña_error.value = "La contraseña es incorrecta"
        else:
            cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (correo.value,))
            user_data = cursor.fetchone()

            page.session.set("usuario", {
                "nombre": user_data[1],
                "correo": user_data[2],
                "telefono": user_data[4] or ""
            })

            go_to_menu()

        cursor.close()
        conn.close()
        page.update()

    titulo = ft.Text("Ingresar", size=30, color="black", weight=ft.FontWeight.BOLD)
    loguear = ft.FilledButton(text="LOGIN", on_click=validar_login)
    registrar = ft.FilledButton(text="Regístrate", on_click=ir_a_registro)

    contenido = ft.Column(
        [titulo, correo, correo_error, contraseña, contraseña_error, loguear, registrar],
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
