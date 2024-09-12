from Paginas.base import PaginaBase
import flet as ft


class PaginaLogin(PaginaBase):
    def __init__(self, on_login, page):
        super().__init__("Login")
        self.on_login = on_login
        self.page = page
        self.page.title = "Login"
        self.page.bgcolor = "#0011A8"

        self.usuario_ref = ft.Ref[ft.TextField]()
        self.senha_ref = ft.Ref[ft.TextField]()
        self.mensagem_erro_ref = ft.Ref[ft.TextField]()

    def renderizar(self):

        container = ft.Container(
            content=ft.Column([
                ft.TextField(label="Usuário", color="Extra Black", ref=self.usuario_ref),
                ft.TextField(label="Senha", color="Extra Black", password=True, can_reveal_password=True, ref=self.senha_ref),
                ft.Text("", ref=self.mensagem_erro_ref, color="red"),
                ft.ElevatedButton(text="Entrar", on_click=self.on_login)
            ], alignment=ft.alignment.center),
            padding=20,
            bgcolor="White",
            border=ft.border.all(2, ft.colors.DEEP_ORANGE),
            border_radius=ft.border_radius.all(15),
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=10,
                color=ft.colors.with_opacity(ft.colors.BLACK, "BLACK"),
                offset=ft.Offset(5, 5)
            ),
            alignment=ft.alignment.center
        )
        return container



    def login(self, _e):
        pass
