#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  :
# Created Date:
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco
from classes.Produto import Produto
from classes.PessoaFisica import PessoaFisica

# Esta classe deverá permitir a inserção de items, bem como a atualização da quantidade de
# produtos em um item

class Carrinho:

    def __init__(self):
        # Chave é o id do Produto e o Valor é a quantidade desse item no carrinho
        self.itens = {}

    def adicionar_item(self, item:Produto, qtd=1):

        if item not in self.itens:
            self.itens[item] = qtd
        else:
            self.itens[item] += qtd
        
        # Implemente a adição do item no dicionário
        
    def get_items(self):
        return self.itens

    def remover_item(self, item:Produto):
        del self.itens[item]
    
    def lista_produtos(self):
        lista_produtos = []
        for item in self.itens:
            lista_produtos += [f'x{self.itens[item]} {item.nome}']       
        return lista_produtos

    def __str__(self):
        pass