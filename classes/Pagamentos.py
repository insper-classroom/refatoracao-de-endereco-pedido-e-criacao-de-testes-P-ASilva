class Pagamento:

    def __init__(self, pedido, método_pag='', parcelas=1, desconto=0): #(self, carrinho, método_pag='', parcelas=1, desconto=0)
        self.método = método_pag
        self.parcelas = parcelas
        self.pedido = pedido
        self.desconto = desconto

    def processa_pagamento(self):
        self.pedido.status = True

    # Função dummy que sempre dá o pagamento como aprovado

    def pagamento_aprovado(self):
        if self.pedido.status == 1:
            return True
        else:
            return False