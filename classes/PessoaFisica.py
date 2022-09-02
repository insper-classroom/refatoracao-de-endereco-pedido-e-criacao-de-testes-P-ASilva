#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

from classes.Endereco import Endereco


class PessoaFisica:
    '''Esta classe implementa uma pessoa no contexto de uma compra em e-commerce.
    
    As propriedades email e cpf estão privadas para previnir o usuário da classe de 
    acessar e alterar diretamente a propriedade sem uma verificação.
    '''
    
    __dict = {}


    def __init__(self, cpf, email, nome='Visitante'):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.enderecos = {}
        PessoaFisica.__dict[nome] = self

    # escolher o estilo de retorno

    def adicionar_endereco(self, apelido_end, end:Endereco):
        self.enderecos[apelido_end] = end

    def remover_endereco(self, apelido_endereco):
        del self.enderecos[apelido_endereco]

    def get_endereco(self, apelido_endereco):
        return self.enderecos[apelido_endereco]
    
    def busca_nome(nome):
        results = []
        for person in PessoaFisica.__dict:
            if person == nome:
                results += [PessoaFisica.__dict[nome]]
        return results

    def listar_enderecos(self):
        ends = self.enderecos
        listagem = []
        for endereco in ends:
            listagem += [ends[endereco]]
        return listagem
    
    def __str__(self):
        if self.nome != '':
            return self.nome
        return self.nome