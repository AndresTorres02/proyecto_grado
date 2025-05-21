import flet as ft
from login import login_view
from registrar import registrar_view

def main(page: ft.Page):
    page.window_width = 400
    page.window_height = 800
    page.window_resizable = False
    page.window_maximizable = False
    page.window_minimizable = False
    page.window_always_on_top = False
    page.update()
    
    def route_change(e):
        page.views.clear()

        if page.route == "/registrar":
            page.views.append(registrar_view(page, volver_login=lambda: page.go("/")))
        else:
            page.views.append(login_view(page, go_to_registrar=lambda: page.go("/registrar")))

        page.update()

    page.on_route_change = route_change
    page.go("/")  # Inicio con Login

ft.app(target=main)


