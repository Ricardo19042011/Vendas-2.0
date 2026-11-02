from InquirerPy import inquirer
import os

def forma_pagamento():
    pagamento = inquirer.select(
        message='Qual a forma de pagamento?',
        choices=['Dinheiro', 'Pix', 'Crédito', 'Débito']
    ).execute()

    return pagamento

venda = {}
venda['Nome'] = input('Nome: ')
venda['Preço'] = float(input('Valor: R$'))
venda['Forma de Pagamento'] = forma_pagamento()

if venda['Forma de Pagamento'] == 'Dinheiro':
    print('DINHEIROOOOOOOOOOOOOOOO')

for chave, valor in venda.items():
    print(f'{chave}: {valor}')