import flet as ft


class PaginaInicial:
    def __init__(self, navegar):
        self.navegar = navegar

    def botao_voltar(self):
        return ft.ElevatedButton(
            text="Voltar",
            on_click=lambda e: self.navegar("PaginaPrincipal")
        )

    def botao_pagina_principal(self):
        return ft.ElevatedButton(
            text="PaginaPrincipal",
            on_click=lambda e: self.navegar("PaginaPrincipal")
        )
