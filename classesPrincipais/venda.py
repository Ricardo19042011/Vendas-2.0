from datetime import date


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

