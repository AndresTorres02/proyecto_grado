import flet as ft  # Se importa la librería Flet para crear la interfaz gráfica

# Función que define la vista "info_detallada"
def info_detallada(page: ft.Page):

    # Función que crea una tarjeta con los datos de un registro
    def crear_tarjeta(imagen, titulo, fecha, info, recomendaciones):
        return ft.Container(
            content=ft.Column([
                # Primera fila: imagen y título con fecha
                ft.Row([
                    # Imagen de la enfermedad
                    ft.Image(src=imagen, width=100, height=100, fit=ft.ImageFit.COVER),
                    # Columna con el título y la fecha del registro
                    ft.Column([
                        ft.Text(titulo, weight=ft.FontWeight.BOLD, color="black"),  # Título en negrita
                        ft.Text(fecha, color="black")  # Fecha
                    ], spacing=5)
                ], spacing=20),
                
                # Texto informativo
                ft.Text("Información", weight=ft.FontWeight.BOLD, color="black"),  # Subtítulo
                ft.Text(info, size=12, color="black"),  # Detalles de la enfermedad
                
                # Texto de recomendaciones
                ft.Text("Recomendaciones", weight=ft.FontWeight.BOLD, color="black"),  # Subtítulo
                ft.Text(recomendaciones, size=12, color="black"),  # Tratamientos recomendados

                # Línea divisoria entre tarjetas
                ft.Divider(height=20, thickness=1)
            ]),
            padding=10  # Espaciado interno de la tarjeta
        )

    # Lista de registros que se mostrarán, cada uno con su tarjeta
    registros = [
        crear_tarjeta("imagenes/pina1.jpg", "Mancha marrón", "20/04/2024",
                      "La mancha marrón está causada por el hongo 'Physalospora ananas'...",
                      "- Aplicar fungicidas con cobre o mancozeb.\n- Podar las hojas afectadas."),
        crear_tarjeta("imagenes/pina2.jpg", "Mancha de la hoja", "17/04/2024",
                      "Condiciones de humedad afectan las hojas...",
                      "- Mejorar el drenaje.\n- Aplicar tratamientos específicos.")
    ]

    # Botón de volver al menú principal
    boton_volver = ft.Container(
        content=ft.GestureDetector(  # Detecta el gesto de clic/tap
            content=ft.Image(
                src="imagenes/turn-left.png",  # Icono de "volver"
                width=40,
                height=40
            ),
            on_tap=lambda e: page.go("/menu")  # Al hacer tap, redirige al menú
        ),
        alignment=ft.alignment.bottom_right,  # Alineado en la esquina inferior derecha
        padding=10  # Espaciado interno
    )

    # Imagen de fondo de la pantalla
    fondo = ft.Image(
        src="imagenes/fondo.jpg",
        fit=ft.ImageFit.COVER,
        width=400,
        height=800
    )

    # Contenedor principal con los registros y el título
    contenido = ft.Container(
        content=ft.Column([
            ft.Text("Registros de mi cultivo", size=20, weight=ft.FontWeight.BOLD, color="black"),  # Título
            ft.ListView(controls=registros, expand=True, spacing=10)  # Lista de tarjetas
        ], spacing=20),
        padding=20,
        width=400,
        height=800,
    )

    # Retorna la vista final apilando el fondo, el contenido y el botón de volver
    return ft.View(
        route="/info",  # Ruta para navegar a esta vista
        controls=[
            ft.Stack([
                fondo,         # Fondo al fondo (valga la redundancia)
                contenido,     # Contenido encima del fondo
                boton_volver   # Botón flotante en la esquina
            ])
        ],
        scroll=ft.ScrollMode.AUTO  # Habilita scroll automático para móviles o pantallas pequeñas
    )
