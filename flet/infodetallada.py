import flet as ft

def info_detallada(page: ft.Page):
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

    registros = [
        crear_tarjeta("imagenes/pina1.jpg", "Mancha marrón", "20/04/2024",
                      "La mancha marrón está causada por el hongo 'Physalospora ananas'...",
                      "- Aplicar fungicidas con cobre o mancozeb.\n- Podar las hojas afectadas."),
        crear_tarjeta("imagenes/pina2.jpg", "Mancha de la hoja", "17/04/2024",
                      "Condiciones de humedad afectan las hojas...",
                      "- Mejorar el drenaje.\n- Aplicar tratamientos específicos.")
    ]

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
        height=800,
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
