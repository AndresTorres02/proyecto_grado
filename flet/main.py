import flet as ft
from login import login_view
from registrar import registrar_view
from mainmenu import menu_principal
from infodetallada import info_detallada
from  crud_user import crud_user 
from resetcontraseña import reset_contraseña_view

# Función principal que se ejecuta al iniciar la aplicación
def main(page: ft.Page):
    # Configura el tamaño de la ventana de la aplicación
    page.window.width = 400        # Ancho fijo de la ventana
    page.window.height = 800       # Alto fijo de la ventana
    page.window.resizable = False  # La ventana no se puede redimensionar
    page.update()                  # Actualiza la interfaz para aplicar los cambios

    # Función que se ejecuta cuando cambia la ruta de navegación
    def route_change(e):
        page.views.clear()  # Limpia todas las vistas anteriores

        # Según la ruta, se muestra la vista correspondiente
        if page.route == "/registrar":
            # Vista de registro con opción de volver al login
            page.views.append(registrar_view(page, volver_login=lambda: page.go("/")))
        elif page.route == "/menu":
            page.views.append(menu_principal(page, 
                                            lambda e: page.go("/info"),# go to info
                                            lambda e: page.go("/crud_user"))) #go to crud_user
        elif page.route == "/crud_user":
            page.views.append(crud_user(page, volver_al_menu=lambda e: page.go("/menu")))

            # Vista del menú principal con opción de ir a la información detallada
            page.views.append(menu_principal(page, go_to_info=lambda: page.go("/info")))
        elif page.route == "/info":
            # Vista de información detallada del cultivo
            page.views.append(info_detallada(page))
        elif page.route == "/reset":
            page.views.append(reset_contraseña_view(page, volver_login=lambda: page.go("/")))
        else:
            # Vista por defecto (login), con navegación a registrar o al menú
            page.views.append(login_view(
                page,
                go_to_registrar=lambda: page.go("/registrar"),
                go_to_menu=lambda: page.go("/menu"),
                go_to_reset=lambda: page.go("/reset")
            ))

        page.update()  # Se actualiza la página con la nueva vista

    page.on_route_change = route_change  # Asocia la función al evento de cambio de ruta
    page.go("/")  # Navega inicialmente a la ruta raíz (login)

# Lanza la aplicación con la función `main` como punto de entrada
ft.app(target=main)
