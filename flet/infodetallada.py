import flet as ft

def info_detallada(page: ft.Page):
    # Función para construir una tarjeta de registro
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
                ft.Divider(height=20, thickness=1, color="grey")
            ]),
            padding=10,
            bgcolor="white",
            border_radius=10
        )

    # Lista de tarjetas de ejemplo
    registros = [
        crear_tarjeta(
            "dataset/sana1.jpg",
            "Mancha marrón",
            "20/04/2024",
            "La mancha marrón de Piña está causada principalmente por el hongo 'Physalospora ananas'...",
            "- Aplicar fungicidas con cobre o mancozeb.\n- Podar para controlar la propagación."
        ),
        crear_tarjeta(
            "dataset/sana1.jpg",
            "Mancha de la hoja (Leaf Spot)",
            "17/04/2024",
            "Causada por condiciones de humedad excesiva que afectan la estructura foliar...",
            "- Usar productos específicos para control de manchas foliares.\n- Mejorar drenaje del cultivo."
        )
        # Puedes agregar más tarjetas aquí
    ]

    # Botón volver abajo a la derecha
        # Botón volver abajo a la derecha (solo clic sobre la imagen)
    boton_volver = ft.Container(
        content=ft.GestureDetector(
            content=ft.Image(
                src="imagenes/turn-left.png",
                width=40,
                height=40
            ),
            on_tap=lambda e: page.go("/menu")
        ),
        alignment=ft.alignment.bottom_right,
        padding=10
    )


    # Contenido sobre el fondo
    contenido_principal = ft.Container(
        content=ft.Column([
            ft.Text("Registros de mi cultivo", size=20, weight=ft.FontWeight.BOLD, color="black"),
            ft.ListView(controls=registros, expand=True, spacing=10),
        ], spacing=20),
        padding=20
    )

    fondo = ft.Stack([
        ft.Image(
            src="imagenes/fondo.jpg",
            fit=ft.ImageFit.COVER,
            width=400,
            height=800
        ),
        contenido_principal,
        boton_volver
    ])

    page.scroll = ft.ScrollMode.AUTO

    return ft.View(
        "/info",
        controls=[
            ft.Container(width=400, height=800, content=fondo)
        ]
    )
