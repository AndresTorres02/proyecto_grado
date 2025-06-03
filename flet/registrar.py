import flet as ft
import mysql.connector

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

    def conectar_bd():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="a1b2c3d4_",
            database="sistema_cultivos"
        )

    def cerrar_dialogo(e):
        dialog.open = False
        page.update()
        volver_login()

    def registrar_usuario(e):
        if contraseña.value != confirmar.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Las contraseñas no coinciden", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()
            return

        try:
            conn = conectar_bd()
            cursor = conn.cursor()

            query = "INSERT INTO usuarios (nombre, correo, contraseña) VALUES (%s, %s, %s)"
            cursor.execute(query, (nombre.value, correo.value, contraseña.value))
            conn.commit()

            dialog.title = ft.Text("Usuario registrado con éxito")
            dialog.open = True
            page.update()

        except mysql.connector.IntegrityError:
            page.snack_bar = ft.SnackBar(
                ft.Text("El correo ya está registrado", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()

        except mysql.connector.Error as err:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Error al registrar: {err}", color="white"),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()

        finally:
            cursor.close()
            conn.close()

    dialog = ft.AlertDialog(
        modal=True,
        actions=[ft.TextButton("OK", on_click=cerrar_dialogo)],
        actions_alignment=ft.MainAxisAlignment.END
    )
    page.dialog = dialog

    titulo = ft.Text("Crear cuenta", size=30, color="white", weight=ft.FontWeight.BOLD)
    correo = ft.TextField(label="Escribe tu correo", color="black", label_style=ft.TextStyle(color="black"))
    nombre = ft.TextField(label="Escribe tu nombre completo", color="black", label_style=ft.TextStyle(color="black"))
    contraseña = ft.TextField(label="Escribe tu contraseña", password=True, color="black", label_style=ft.TextStyle(color="black"))
    confirmar = ft.TextField(label="Confirmar contraseña", password=True, color="black", label_style=ft.TextStyle(color="black"))
    crear = ft.FilledButton(text="CREAR", on_click=registrar_usuario)
    volver = ft.FilledButton(text="Volver al Login", on_click=regresar)

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
                ft.Container(content=contenido, padding=30),
                dialog
            ])
        ]
    )
