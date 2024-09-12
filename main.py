import flet as ft
from Paginas.pagina_cadastro_cliente import PaginaCadCliente
from Paginas.pagina_login import PaginaLogin
from Paginas.pagina_principal import PaginaPrincipal
from Paginas.cadastro_usuario import PaginaCadUsuario


def main(page: ft.Page):

    def navegar(nome_pagina):
        print(f"Criando a navegação {nome_pagina}")
        page.controls.clear()

        if nome_pagina == "Login":
            print(f"Navegando para {nome_pagina}")
            page.add(PaginaLogin(on_login=lambda _: navegar("PaginaPrincipal"), page=page).renderizar())
        elif nome_pagina == "PaginaPrincipal":
            print(f"Navegando para {nome_pagina}")
            page.add(PaginaPrincipal(on_navegation=navegar, navegar=navegar, page=page).renderizar())
        elif nome_pagina == "CadastrarCliente":
            print(f"Navegando para pagina cadastro clientes")
            page.add(PaginaCadCliente(navegar=navegar, page=page).renderizar())
        elif nome_pagina == "CadastrarUsuario":
            print(f"Navegando para pagina cadastro usuarios")
            page.add(PaginaCadUsuario(navegar=navegar, page=page).renderizar())
        page.update()
    navegar("Login")


if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP)
