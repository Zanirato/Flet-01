import flet as ft

def main(page: ft.Page):
    page.title = "Seletor de Cores"
    page.padding = 20

    # Container que mudará de cor
    caixa_colorida = ft.Container(
        content=ft.Text(
            "Escolha uma cor",
            color=ft.Colors.WHITE,
            size=18,
            text_align=ft.TextAlign.CENTER
        ),
        bgcolor=ft.Colors.GREY, # Cor inicial
        width=300,
        height=100,
        border_radius=10, # Bordas arredondadas
        alignment=ft.alignment.center # Centraliza o texto dentro da caixa
    )

    def cor_selecionada(evento):
        """
        Esta função é executada sempre que o usuário escolhe uma cor.
        """
        # Pegando qual cor foi selecionado
        cor_selecionada = evento.control.value

        # Dicionário com as cores disponíveis
        # É como uma "lista de correspondência" entre nome e cor real
        cores_disponiveis = {
            "Azul": ft.Colors.BLUE,
            "Vermelho": ft.Colors.RED,
            "Verde": ft.Colors.GREEN,
            "Amarelo": ft.Colors.YELLOW,
            "Roxo": ft.Colors.PURPLE,
            "Laranja": ft.Colors.ORANGE,
            "Cinza": ft.Colors.GREY,
            "Rosa": ft.Colors.PINK,
            "Preto": ft.Colors.BLACK,
            "Branco": ft.Colors.WHITE
        }

        # Mudando a cor do container para a cor selecionada
        caixa_colorida.bgcolor = cores_disponiveis[cor_selecionada]
        caixa_colorida.content.value = f"Cor selecionada: {cor_selecionada} ⭐"

        page.update()

    # Criando a lista suspensa (dropdown)
    seletor_cor = ft.Dropdown(
        label="Selecione uma cor",
        width=200,
        options=[
            ft.dropdown.Option("Azul"),
            ft.dropdown.Option("Vermelho"),
            ft.dropdown.Option("Verde"),
            ft.dropdown.Option("Amarelo"),
            ft.dropdown.Option("Roxo"),
            ft.dropdown.Option("Laranja"),
            ft.dropdown.Option("Cinza"),
            ft.dropdown.Option("Rosa"),
            ft.dropdown.Option("Preto"),
            ft.dropdown.Option("Branco")
        ],
        on_change=cor_selecionada # Função chamada quando a cor é selecionada
    )

    # Adicionando os elementos na página
    page.add(
        ft.Text("Seletor de Cores Mágicos ⭐", size=24, weight=ft.FontWeight.BOLD),
        seletor_cor,
        caixa_colorida
    )

ft.app(target=main)