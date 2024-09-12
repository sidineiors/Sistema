from flet_core import CrossAxisAlignment
from Paginas.base import PaginaBase
import flet as ft


class PaginaPrincipal(PaginaBase):
    def __init__(self,on_navegation, navegar, page):
        super().__init__("PaginaPrincipal")
        self.on_navegation=on_navegation
        self.navegar = navegar
        self.page = page
        self.page.favicon = "favicon.png"
        self.page.title = "S&P Auto Elétrica"
        self.valor_caixa = 0

    def abrir_caixa(self, _e):
        def salvar_valor(_e):
            try:
                self.valor_caixa = float(valor_input.value)
                dialog.open = False
                self.page.update()
                self.navegar("FluxoCaixa")
            except ValueError:
                self.page.snack_bar = ft.SnackBar(ft.Text("Insira um valor númerico!,"))
                self.page.snack_bar.open = True
                self.page.update()

        valor_input = ft.TextField(label="Valor em Caixa", keyboard_type=ft.KeyboardType.NUMBER)

        dialog = ft.AlertDialog(
            title=ft.Text("Abrir Caixa"),
            content=ft.Column([valor_input]),
            actions=[ft.ElevatedButton("Salvar",on_click=salvar_valor)],
            open=True,
        )
        self.page.dialog = dialog
        self.page.update()


    def renderizar(self):

        container = ft.Container(
            content=ft.Column([
                ft.Text(value="SeP Auto Elétrica", color="White"),
                ft.Stack([
                    ft.CircleAvatar(
                        background_image_url=
                        "https://scontent.fitp1-1.fna.fbcdn.net/v/t39.30808-6/449855800_2222735374738667_1328454966500185412_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeHrDLe73q6Px--qev1vC-A0cSCtlre-qW9xIK2Wt76pb0z-kgYk6LwwO_iWsM6Jf1TrjU8jKehHGNqzR9_XHKM4&_nc_ohc=9oi8sas-0E4Q7kNvgGAX7kx&_nc_ht=scontent.fitp1-1.fna&_nc_gid=Al2KJrzCrrVRGhlHe6rtL8g&oh=00_AYDRfIp8Jq3PyQPFBobimlT5ARG4S6xaI6xz2qJOfmnPEQ&oe=66E68245"
                    ),
                ft.Container(
                    content=ft.CircleAvatar(bgcolor=ft.colors.GREEN, radius=5),
                    alignment=ft.alignment.bottom_left
                )
                ]),
                ft.Row([
                ft.ElevatedButton(text="Abrir Caixa", on_click=self.abrir_caixa),
                ft.ElevatedButton(text="Cadastrar Cliente", on_click=lambda _: self.navegar("CadastrarCliente")),
                ft.ElevatedButton(text="Fluxo de Caixa", on_click=lambda _: self.navegar("FluxoCaixa")),
                ft.ElevatedButton(text="Cadastrar Usuario", on_click=lambda _: self.navegar("CadastrarUsuario")),
                ft.ElevatedButton(text="Cadastrar Produto", on_click=lambda _: self.navegar("CadastrarProdutos")),
                ],alignment=ft.MainAxisAlignment.CENTER,
                spacing=10)
            ],alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.START,
            ),
            padding=20,
            bgcolor="#0011A8",
            border=ft.border.all(2, ft.colors.DEEP_ORANGE),
            border_radius=ft.border_radius.all(15),
            shadow=ft.BoxShadow(
                spread_radius=5,
                blur_radius=10,
                color=ft.colors.with_opacity(ft.colors.BLACK, "Black"),
                offset=ft.Offset(5, 5)
            ),
            alignment=ft.alignment.bottom_left
        )
        return container
