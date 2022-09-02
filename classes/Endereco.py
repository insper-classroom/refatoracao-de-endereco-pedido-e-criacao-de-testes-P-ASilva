#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Tiago Sanches da Silva e Fabio Miranda - https://github.com/Tiagoeem | https://github.com/mirwox
# Created Date: 15/08/2022
# version ='1.0'
# ---------------------------------------------------------------------------

import requests
import json
import numpy as np


class Endereco: 
    '''
    Endereço de uma pessoa ou conta.
    Esta classe possui overload de Contrutor, caso envie apenas três parametros será encaminhado
    para o contrutor que consulta o cep para encontrar o endereço.
    '''
    
    def __init__(cls, cep, numero ,rua='', estado='', cidade='', complemento=''):

        if (rua == '') or (estado == '') or (cidade == ''):
            cep = Endereco.check_and_fix_cep_sintax(cep)

            end_json =  cls.consultar_cep(cep)

            cls.rua = end_json['logradouro']
            cls.estado = end_json['uf']
            cls.cidade = end_json['localidade']
            cls.numero = numero
            cls.complemento = complemento
            cls.cep = str(cep)

        else:

            cls.rua = rua
            cls.estado = estado
            cls.cidade = cidade
            cls.numero = int(numero)
            cls.complemento = complemento
            cls.cep = str(cep)

    @classmethod
    def consultar_cep(cls, cep):
        '''
        Metodo realiza a consulta do cep em uma api publica para obter informações
        como estado, cidade e rua
        '''
        # continuam existindo variaveis locais, nem tudo é propriedade de objeto

        # end point da API de consulta ao cep

        cep = Endereco.check_and_fix_cep_sintax(cep)

        if cep == False:
            return False

        url_api = f'https://viacep.com.br/ws/{str(cep)}/json/'

        # Sem corpo na requisição
        # Não é necessario nenhum cabeçalho HTTP especial
        payload = {}
        headers = {}

        # requisição GET na url de pesquisa do cep. Doc.: https://viacep.com.br/
        response = requests.request("GET", url_api, headers=headers, data=payload)
        # converte a resposta json em dict
        json_resp = response.json()
        if json_resp == {'erro': 'true'}:
            return False
        return json_resp

    def check_and_fix_cep_sintax(cep): # Done
        cep = str(cep)
        if len(cep) <= 8:
                while len(cep) < 8:
                    cep = f'0{cep}'
                return cep
        else:
            print('oohh shit')
            return False

    def __str__ (cls):
        return f' {cls.rua}, {cls.numero} --- {cls.cidade} --- {cls.estado}'