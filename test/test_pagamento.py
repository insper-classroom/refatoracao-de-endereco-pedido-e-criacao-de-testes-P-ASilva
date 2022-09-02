from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import requests

@pytest.mark.test_pag
def test_cria_pagamento():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    carrinho = Carrinho()
    pedido = Pedido(carrinho,pessoa1)
    pag = Pagamento(pedido)
    assert pag.pedido == pedido

@pytest.mark.test_pag
def test_processa_pag():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    carrinho = Carrinho()
    pedido = Pedido(carrinho,pessoa1)
    pag = Pagamento(pedido)
    pag.processa_pagamento()

    assert pag.pedido.status == Pedido.PAGO

@pytest.mark.test_pag
def test_pedido_nao_pago():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    carrinho = Carrinho()
    pedido2 = Pedido(carrinho,pessoa1)
    assert pedido2.status == 0