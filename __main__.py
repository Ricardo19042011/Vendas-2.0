#'Adicionar venda' 'Remover venda' 'Ver vendas' 'Editar venda' 'Busca por nome' 'Busca por data' 'Limpar vendas' 'Sair'

from funcoes.cadastro import cadastrar_venda
from classesPrincipais.gerenciador_vendas import GerenciadorVendas
from funcoes.funcoesExtras import menu
import os

gerenciador = GerenciadorVendas()

def main():
    while True:
        menu_principal = menu()

        if menu_principal == 'Adicionar venda':
            os.system("cls" if os.name == "nt" else "clear")
            cadastrar_venda(gerenciador=gerenciador)
            





if __name__ == '__main__':
    main()