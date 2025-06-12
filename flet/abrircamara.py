import flet as ft
import cv2
import tempfile
import os

def abrir_camara(page: ft.Page, go_back):


    img_control = ft.Image()
    temp_dir = tempfile.gettempdir()
    temp_image_path = os.path.join(temp_dir, "captura.jpg")

    def tomar_foto(e):
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            page.snack_bar = ft.SnackBar(ft.Text("No se pudo acceder a la cámara."))
            page.snack_bar.open = True
            page.update()
            return

        ret, frame = cap.read()
        cap.release()

        if ret:
            cv2.imwrite(temp_image_path, frame)
            img_control.src = temp_image_path
            img_control.update()
            contenedor_foto.visible = True
            btn_tomar.visible = False
            btn_aceptar.visible = True
            btn_repetir.visible = True
            page.update()
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Error al tomar la foto."))
            page.snack_bar.open = True
            page.update()

    def aceptar_foto(e):
        page.snack_bar = ft.SnackBar(ft.Text("Foto aceptada."))
        page.snack_bar.open = True
        page.update()
        go_back()  # vuelve a menu 

    def tomar_otra(e):
        contenedor_foto.visible = False
        btn_tomar.visible = True
        btn_aceptar.visible = False
        btn_repetir.visible = False
        img_control.src = ""
        page.update()

    btn_tomar = ft.ElevatedButton("Tomar Foto", on_click=tomar_foto)
    btn_aceptar = ft.ElevatedButton("Aceptar", on_click=aceptar_foto, visible=False)
    btn_repetir = ft.ElevatedButton("Tomar Otra", on_click=tomar_otra, visible=False)

    contenedor_foto = ft.Container(content=img_control, visible=False)

    return ft.View(
        route="/abrir_camara",
        controls=[
            ft.Column(
                [
                    ft.Text("Cámara", size=24, weight=ft.FontWeight.BOLD),
                    btn_tomar,
                    contenedor_foto,
                    ft.Row([btn_repetir, btn_aceptar], alignment=ft.MainAxisAlignment.CENTER)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        ],
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
