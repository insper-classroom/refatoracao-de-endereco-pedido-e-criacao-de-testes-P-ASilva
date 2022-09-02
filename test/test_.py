from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import requests

@pytest.mark.test_end
def test_cep_como_int():
    end1 = Endereco(int('08320330') , 430)
    end2 = Endereco('08320330' , 430)
    assert  end2.consultar_cep(end2.cep) == end1.consultar_cep(end1.cep)


@pytest.mark.test_end
def test_cep_nao_existe():
    assert False == Endereco.consultar_cep(99999999)

@pytest.mark.test_end
def test_cep_mto_longo():
    assert False == Endereco.consultar_cep(999999999999)

@pytest.mark.test_end
def test_cria_endereco():
    end2 = Endereco('08320330' , 430)
    assert '08320330' == end2.cep
    assert 430 == end2.numero

@pytest.mark.test_SC
@pytest.mark.test_end
def test_cep_falha_de_conexao():
    with pytest.raises(requests.exceptions.ConnectionError):
        Endereco('08320330' , 430)

@pytest.mark.test_pf
def test_cria_pessoa_fisica():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')

    assert 'Carlos' == pessoa1.nome
    assert 'tiago@email.com' == pessoa1.email
    assert '524.222.452-6' == pessoa1.cpf

@pytest.mark.test_prod
def test_cria_produto():
    prod1 = Produto("0010342967", "Sabonete")
    assert "0010342967" == prod1.id
    assert "Sabonete" == prod1.nome

@pytest.mark.test_cr
def test_cria_e_adiciona_ao_carrinho():
    prod1 = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()
    assert carrinho.itens == {}
    carrinho.adicionar_item(prod1)
    assert carrinho.itens == {prod1:1}

@pytest.mark.test_ped
def test_cria_pedido():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    carrinho = Carrinho()
    pedido = Pedido(carrinho,pessoa1)
    assert carrinho == pedido.carrinho
    assert pessoa1 == pedido.comprador

@pytest.mark.test_pag
def test_cria_pagamento():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    carrinho = Carrinho()
    pedido = Pedido(carrinho,pessoa1)
    pag = Pagamento(pedido)
    assert pag.pedido == pedido