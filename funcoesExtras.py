from InquirerPy import inquirer

def Sim_Não():
    escolha = inquirer.select(
        message='Tem certeza?',
        choices=['Sim', 'Não']
        ).execute()
    return escolha


def forma_pagamento():
    pagamento = inquirer.select(
        message='Qual a forma de pagamento?',
        choices=['Dinheiro', 'Pix', 'Crédito', 'Débito']
    ).execute()
    return pagamento


def menu():
    opcoes = inquirer.select(
        message='O que deseja fazer agora?',
        choices=['Adicionar venda', 'Remover venda', 'Ver vendas', 'Editar venda', 
                'Busca por nome', 'Busca por data', 'Limpar vendas', 'Sair']
    ).execute()
    return opcoes


