import os

from rich import print

from funcoes.funcoesExtras import forma_pagamento
from classesPrincipais.venda import Venda


def cadastrar_venda(gerenciador):
    while True:
        nome = input('Nome: ').strip().capitalize()
        if not nome:
            os.system("cls" if os.name == "nt" else "clear")
            print("[red]O nome não pode ficar vazio.[/red]")
            continue
        else:
            break

    while True:
        try:
            preco = float(input("Preço: R$").replace(",", "."))
        except ValueError:
            os.system("cls" if os.name == "nt" else "clear")
            print('[red]Valor inválido. Tente novamente![/red]')
            continue
        else:
            if preco <= 0:
                os.system("cls" if os.name == "nt" else "clear")
                print("[red]O preço deve ser maior que zero.[/red]")
                continue
            forma_Pagamento = forma_pagamento()
            venda = Venda(nome=nome, preco=preco, forma_pagamento=forma_Pagamento)
            gerenciador.adicionar(venda=venda)
            os.system("cls" if os.name == "nt" else "clear")
            break
