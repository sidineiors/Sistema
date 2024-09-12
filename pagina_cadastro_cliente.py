from Paginas.base import PaginaBase
from Componentes.botao_navegacao import BotaoNavegacao
from Paginas.Formularios.verificacao_campos import ValidadorCampos
import flet as ft

class PaginaCadCliente(PaginaBase):
    def __init__(self, navegar, page):
        super().__init__("CadastrarCliente")
        self.navegar = navegar
        self.page = page
        self.page.title = "Cadastro de Clientes"
        
        self.input_nome = ft.TextField(label="Nome", color="Black")
        self.input_email = ft.TextField(label="Email", color="Black")
        self.cpf_input = ft.TextField(label="CPF/123.456.789-10", color="Black")
        self.endereco_input = ft.TextField(label="Endereço", color="Black")
        self.telefone_input = ft.TextField(label="Cel/(00)999.999999")

        self.mensagem_erro = ft.Text(value="", color="Red")

    def validar_dados(self):
        erros = []

        erros_nome = ValidadorCampos.validar_campos_alfabeticos(self.input_nome.value)
        if erros_nome:
            erros.append(erros_nome)

        erros_email = ValidadorCampos.validar_email(self.input_email.value)
        if erros_email:
            erros.append(erros_email)

        erros_cpf = ValidadorCampos.validar_cpf(self.cpf_input)
        if erros_cpf:
            erros.append(erros_cpf)

        erros_endereco = ValidadorCampos.validar_campos_alfabeticos(self.endereco_input.value)
        if erros_endereco:
            erros.append(erros_endereco)

        erros_telefone = ValidadorCampos.validar_telefone(self.telefone_input)
        if erros_telefone:
            erros.append(erros_telefone)

        if erros:
            self.mensagem_erro.value = "\n".join(erros)
            self.page.update()
            return False
        return True

    def enviar_formulario(self, _e):
        if self.validar_dados():
            print("Dados válidos, seguir com processo!")
        else:
            print("Erro ao válidar dados!")

    def renderizar(self):
        container = ft.Container(
            content=ft.Column([
                ft.Text(value="Cadastrar Cliente", color="Blue"),
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
                self.input_nome,
                self.input_email,
                self.cpf_input,
                self.endereco_input,
                self.telefone_input,
                self.mensagem_erro,
                ft.ElevatedButton(text="Cadastrar cliente"),
                ft.Row([
                    BotaoNavegacao(navegar=self.navegar, voltar_pagina_principal=True).build()
                ],alignment=ft.alignment.center,
                spacing=10),
            ], alignment=ft.alignment.center,
               spacing=10),
            padding=20,
            bgcolor="White",
            border=ft.border.all(2, ft.colors.DEEP_ORANGE),
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
