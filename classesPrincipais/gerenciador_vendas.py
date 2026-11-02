class GerenciadorVendas:
    def __init__(self):
        self.lista = []

    def adicionar(self, venda):
        dados = venda.para_dicionario()
        self.lista.append(dados)

    def remover(self):
        pass

