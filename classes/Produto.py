#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------



class Produto:

    __dict = {}

    def __init__(self, id_prod, nome_prod, price = 0.00):
        self.id = id_prod
        self.nome = nome_prod
        Produto.__dict[nome_prod] = self

    def change_id(self,new_id):
        self.id = new_id

    def get_id(self):
        return self.id

    def change_name(self, new_name):
        self.nome = new_name

    def get_name(self):
        return self.nome

    def busca_nome(nome):
        results = []
        for person in Produto.__dict:
            if person == nome:
                results += [Produto.__dict[nome]]
        return results

    def __str__(self):
        return f'{self.nome} [ID:{self.id}]'