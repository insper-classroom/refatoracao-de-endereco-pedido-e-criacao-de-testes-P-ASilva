#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Pagamentos import Pagamento
from classes.PessoaFisica import PessoaFisica
from classes.Carrinho import Carrinho
import re




class Pedido:

    def __init__(self, carrinho=Carrinho, comprador=PessoaFisica):
        self.carrinho = carrinho
        self.comprador = comprador
        self.endereco_entrega = ''
        self.endereco_faturamento = ''
        self.status = 0

    PAGO = 1
    PENDENTE = 0

    def __str__(self): 
        return f'{self.comprador} --- {self.endereco_entrega} --- {self.carrinho.lista_produtos()}'