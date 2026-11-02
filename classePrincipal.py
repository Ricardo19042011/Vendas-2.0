from datetime import date
from funcoesExtras import forma_pagamento

class Venda:
    def __init__(self, nome, preco, forma_pagamento):
        self.nome = nome
        self.preco = preco
        self.forma_pagamento = forma_pagamento
        self.data_venda = date.today().strftime("%d/%m/%Y")

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "forma_pagamento": self.forma_pagamento,
            "data_venda": self.data_venda
        }


class GerenciadorVendas:
    def __init__(self):
        self.lista = []

    def adicionar(self, venda):
        dados = venda.para_dicionario()
        self.lista.append(dados)

    def remover(self):
        pass


gerenciador = GerenciadorVendas()

def cadastrar_venda(gerenciador):
    nome = input('Nome: ')
    preco = float(input('Preço: R$'))
    forma_Pagamento = forma_pagamento()
    venda = Venda(nome=nome, preco=preco, forma_pagamento=forma_Pagamento)
    gerenciador.adicionar(venda=venda) 


print(gerenciador.lista)