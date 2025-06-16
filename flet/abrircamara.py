import flet as ft
import cv2
import tempfile
from predecir import predecir_imagen
import os
from condiciones import obtener_condiciones
from crud_diagnosticos import insertar_diagnostico  # O desde donde tengas la función
from datetime import datetime

def abrir_camara(page: ft.Page, go_back):

    img_control = ft.Image()
    ruta_ultima_imagen = ""

    carpeta_imagenes = os.path.join(os.getcwd(), "imagenes_tomadas")
    os.makedirs(carpeta_imagenes, exist_ok=True)

    def generar_nombre_imagen():
        archivos = os.listdir(carpeta_imagenes)
        numeros = [int(f.split(".")[0]) for f in archivos if f.endswith(".jpg") and f.split(".")[0].isdigit()]
        siguiente_numero = max(numeros) + 1 if numeros else 1
        return os.path.join(carpeta_imagenes, f"{siguiente_numero}.jpg")

    def tomar_foto(e):
        nonlocal ruta_ultima_imagen

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            page.snack_bar = ft.SnackBar(ft.Text("No se pudo acceder a la cámara."))
            page.snack_bar.open = True
            page.update()
            return

        ret, frame = cap.read()
        cap.release()

        if ret:
            nombre_imagen = generar_nombre_imagen()
            cv2.imwrite(nombre_imagen, frame)
            ruta_ultima_imagen = nombre_imagen
            img_control.src = nombre_imagen
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
        if ruta_ultima_imagen and os.path.exists(ruta_ultima_imagen):
            prediccion, confianza = predecir_imagen(ruta_ultima_imagen)
            
            # Obtener nombre de la foto
            nombre_foto = os.path.basename(ruta_ultima_imagen)
            enfermedad_detectada = prediccion
            
            # Obtener información adicional desde condiciones.py
            fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fecha, enfermedad, info_detallada, tratamiento = obtener_condiciones(nombre_foto, enfermedad_detectada)

            # Número de foto = cuántas hay en la carpeta
            numero_foto = len(os.listdir("imagenes_tomadas"))

            # Guardar en base de datos

            correo_usuario = page.session.get("usuario")["correo"]

            insertar_diagnostico(
                nombre_foto=nombre_foto,
                fecha=fecha_actual,
                nombre_enfermedad=enfermedad,
                info_detallada=info_detallada,
                tratamiento=tratamiento,
                correo_usuario=correo_usuario
            )

            # Mostrar resultado
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Resultado: {prediccion} ({confianza:.2f}% de confianza). Guardado en base de datos.")
            )
        else:
            page.snack_bar = ft.SnackBar(
                ft.Text("No se encontró la imagen para analizar.")
            )

        page.snack_bar.open = True
        page.update()
        go_back()


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
