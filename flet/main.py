import flet as ft
from login import login_view
from registrar import registrar_view
from mainmenu import menu_principal
from infodetallada import info_detallada

def main(page: ft.Page):
    page.window.width = 400        # window's width is 200 px
    page.window.height = 800       # window's height is 200 px
    page.window.resizable = False  # window is not resizable
    page.update()
        
    def route_change(e):
        page.views.clear()

        if page.route == "/registrar":
            page.views.append(registrar_view(page, volver_login=lambda: page.go("/")))
        elif page.route == "/menu":
            page.views.append(menu_principal(page, go_to_info=lambda: page.go("/info")))
        elif page.route == "/info":
            page.views.append(info_detallada(page))
        else:
            page.views.append(login_view(
                page,
                go_to_registrar=lambda: page.go("/registrar"),
                go_to_menu=lambda: page.go("/menu")
            ))

        page.update()

    page.on_route_change = route_change
    page.go("/")  # Inicio con Login

ft.app(target=main)
