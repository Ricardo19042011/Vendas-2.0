#'Adicionar venda' 'Remover venda' 'Ver vendas' 'Editar venda' 'Busca por nome' 'Busca por data' 'Limpar vendas' 'Sair'


from funcoesExtras import menu
import os


def main():
    while True:
        menu_principal = menu()

        if menu_principal == 'Adicionar venda':
            os.system("cls" if os.name == "nt" else "clear")
            print('cu')
            





if __name__ == '__main__':
    main()