from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import requests



@pytest.mark.test_pf
def test_cria_pessoa_fisica():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')

    assert 'Carlos' == pessoa1.nome
    assert 'tiago@email.com' == pessoa1.email
    assert '524.222.452-6' == pessoa1.cpf

@pytest.mark.test_pf
def test_listar_enderecos_inexistente():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    assert pessoa1.listar_enderecos() == []

@pytest.mark.test_pf
def test_listar_enderecos_um():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    end1 = Endereco('08320330', 430)
    pessoa1.adicionar_endereco('casa', end1)
    assert pessoa1.listar_enderecos() == [end1]

@pytest.mark.test_pf
def test_buscar_nome_um_resultado():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    pessoas = PessoaFisica.busca_nome('Carlos')
    assert len(pessoas) == 1
    assert pessoas[0].email == pessoa1.email