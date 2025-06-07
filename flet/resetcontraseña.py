import flet as ft
import mysql.connector

def reset_contraseña_view(page: ft.Page, volver_login):

    # Conectar a la base de datos
    def conectar_bd():
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="a1b2c3d4_",
            database="sistema_cultivos"
        )

    correo = ft.TextField(label="Correo", border_color="grey", color="black")
    correo_helper = ft.Text("", size=12, color="red")

    pregunta = ft.Text("")  # Se llenará dinámicamente
    respuesta = ft.TextField(label="Respuesta de seguridad", border_color="grey", color="black", visible=False)
    respuesta_helper = ft.Text("", size=12, color="red")

    nueva_contra = ft.TextField(label="Nueva contraseña", password=True, border_color="grey", color="black", visible=False)
    confirmar_contra = ft.TextField(label="Confirmar contraseña", password=True, border_color="grey", color="black", visible=False)
    contra_helper = ft.Text("", size=12, color="red")

    btn_verificar = ft.ElevatedButton(text="Verificar correo", on_click=lambda e: verificar_correo())
    btn_validar_respuesta = ft.ElevatedButton(text="Validar respuesta", on_click=lambda e: validar_respuesta(), visible=False)
    btn_cambiar = ft.FilledButton(text="Cambiar contraseña", on_click=lambda e: cambiar_contraseña(), visible=False)
    btn_volver = ft.TextButton(text="Volver al login", on_click=lambda e: volver_login())

    # Verificar si el correo está registrado y obtener su pregunta
    def verificar_correo():
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT pregunta FROM usuarios WHERE correo = %s", (correo.value,))
            result = cursor.fetchone()

            if result:
                pregunta.value = f"Pregunta de seguridad: {result[0]}"
                respuesta.visible = True
                btn_validar_respuesta.visible = True
                correo.border_color = "grey"
                correo_helper.value = ""
            else:
                correo.border_color = "red"
                correo_helper.value = "Correo no encontrado"

            page.update()
        finally:
            cursor.close()
            conn.close()

    # Validar respuesta de seguridad
    def validar_respuesta():
        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("SELECT info_pregunta FROM usuarios WHERE correo = %s", (correo.value,))
            resultado = cursor.fetchone()

            if resultado and resultado[0].strip().lower() == respuesta.value.strip().lower():
                nueva_contra.visible = True
                confirmar_contra.visible = True
                btn_cambiar.visible = True
                respuesta.border_color = "grey"
                respuesta_helper.value = ""
            else:
                respuesta.border_color = "red"
                respuesta_helper.value = "Respuesta incorrecta"

            page.update()
        finally:
            cursor.close()
            conn.close()

    # Cambiar la contraseña
    def cambiar_contraseña():
        contra_helper.value = ""

        if nueva_contra.value != confirmar_contra.value:
            contra_helper.value = "Las contraseñas no coinciden"
            nueva_contra.border_color = "red"
            confirmar_contra.border_color = "red"
            page.update()
            return

        try:
            conn = conectar_bd()
            cursor = conn.cursor()
            cursor.execute("UPDATE usuarios SET contraseña = %s WHERE correo = %s",
                           (nueva_contra.value, correo.value))
            conn.commit()

            # Mostrar mensaje y volver
            page.snack_bar = ft.SnackBar(ft.Text("Contraseña cambiada con éxito", color="white"), bgcolor="green")
            page.snack_bar.open = True
            page.update()
            volver_login()

        finally:
            cursor.close()
            conn.close()

    # Controles visuales
    contenido = ft.Column([
        ft.Text("Recuperar contraseña", size=28, weight=ft.FontWeight.BOLD, color="white"),
        correo,
        correo_helper,
        btn_verificar,
        pregunta,
        respuesta,
        respuesta_helper,
        btn_validar_respuesta,
        nueva_contra,
        confirmar_contra,
        contra_helper,
        btn_cambiar,
        btn_volver
    ], alignment=ft.MainAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO)

    return ft.View(
        route="/reset",
        controls=[
            ft.Stack([
                ft.Image(src="imagenes/fondo.jpg", fit=ft.ImageFit.COVER, width=400, height=800),
                ft.Container(content=contenido, padding=30)
            ])
        ]
    )
