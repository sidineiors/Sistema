from Paginas.base import PaginaBase
from Componentes.botao_navegacao import BotaoNavegacao
import flet as ft


class PaginaCadUsuario(PaginaBase):
    def __init__(self, navegar, page):
        super().__init__("CadastrarUsuario")
        self.navegar = navegar
        self.page = page
        self.page.title = "Cadastro de Usuário"

    def renderizar(self):
        container=ft.Container(
            content=ft.Column([
                ft.Text("Cadastro de Usuário"),
                ft.TextField(label="Informe o nome do usuário", color="Black"),
                ft.TextField(label="Cpf(123.456.789-10)", color="Black"),
                ft.TextField(label="Email"),
                ft.TextField(label="Tel/Cel"),
                BotaoNavegacao(navegar=self.navegar, voltar_pagina_principal=True).build()
            ],alignment=ft.alignment.center,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=20,
            bgcolor="White",
            border=ft.border.all(2,ft.colors.DEEP_ORANGE),
            border_radius=ft.border_radius.all(15),
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=10,
                color=ft.colors.with_opacity(ft.colors.BLACK, "Black"),
                offset=ft.Offset(5,5)
            ),
            alignment=ft.alignment.bottom_left
        )
        return container
