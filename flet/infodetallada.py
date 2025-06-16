import flet as ft
from crud_diagnosticos import obtener_diagnosticos  # Asegúrate de importar la función correctamente

def info_detallada(page: ft.Page):
    # Usamos session para obtener el correo del usuario
    usuario = page.session.get("usuario")
    if not usuario or "correo" not in usuario:
        print("Error: No se encontró el correo del usuario en sesión.")
        return ft.View(
            route="/info",
            controls=[ft.Text("Error: No se encontró el correo del usuario en sesión.")],
        )

    correo_usuario = usuario["correo"]
    print("Usuario en sesión al entrar:", correo_usuario)

    # Función que crea una tarjeta con los datos de un registro
    def crear_tarjeta(imagen, titulo, fecha, info, recomendaciones):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Image(src=imagen, width=100, height=100, fit=ft.ImageFit.COVER),
                    ft.Column([
                        ft.Text(titulo, weight=ft.FontWeight.BOLD, color="black"),
                        ft.Text(fecha, color="black")
                    ], spacing=5)
                ], spacing=20),
                ft.Text("Información", weight=ft.FontWeight.BOLD, color="black"),
                ft.Text(info, size=12, color="black"),
                ft.Text("Recomendaciones", weight=ft.FontWeight.BOLD, color="black"),
                ft.Text(recomendaciones, size=12, color="black"),
                ft.Divider(height=20, thickness=1)
            ]),
            padding=10
        )

    # Cargar los registros desde la base de datos
    registros = []
    try:
        resultados = obtener_diagnosticos(correo_usuario)
        for registro in resultados:
            imagen_path = f"imagenes_tomadas/{registro['nombre_foto']}"
            registros.append(
                crear_tarjeta(
                    imagen=imagen_path,
                    titulo=registro["nombre_enfermedad"],
                    fecha=registro["fecha"],
                    info=registro["info_detallada"],
                    recomendaciones=registro["tratamiento"]
                )
            )
    except Exception as e:
        print("Error al cargar registros:", e)
        registros.append(ft.Text("No se pudieron cargar los registros.", color="red"))

    boton_volver = ft.Container(
        content=ft.GestureDetector(
            content=ft.Image(src="imagenes/turn-left.png", width=40, height=40),
            on_tap=lambda e: page.go("/menu")
        ),
        alignment=ft.alignment.bottom_right,
        padding=10
    )

    fondo = ft.Image(
        src="imagenes/fondo.jpg",
        fit=ft.ImageFit.COVER,
        width=400,
        height=800
    )

    contenido = ft.Container(
        content=ft.Column([
            ft.Text("Registros de mi cultivo", size=20, weight=ft.FontWeight.BOLD, color="black"),
            ft.ListView(controls=registros, expand=True, spacing=10)
        ], spacing=20),
        padding=20,
        width=400,
        height=800
    )

    return ft.View(
        route="/info",
        controls=[
            ft.Stack([
                fondo,
                contenido,
                boton_volver
            ])
        ],
        scroll=ft.ScrollMode.AUTO
    )
