from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import requests
import copy

# Alguns testes de integração estão nos arquivos de classe (Por ex: Pedido e Pagamento), visto que elas são baseadas nela.

@pytest.mark.test_cr
@pytest.mark.test_integrationM2
def test_adiciona_produto__ao_carrinho():
    prod1 = Produto("0010342967", "Sabonete")
    carrinho = Carrinho()

    carrinho.adicionar_item(prod1)
    assert carrinho.itens == {prod1:1}

@pytest.mark.test_pf
@pytest.mark.test_integrationM2
def test_adiciona_endereco_a_pessoa():
    end1 = Endereco('08320330', 430)
    end2 = Endereco('04546042', 300)
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    pessoa1.adicionar_endereco('casa', end1)
    assert pessoa1.enderecos == {'casa':end1}

@pytest.mark.test_ped
@pytest.mark.test_integrationM2
def test_adiciona_endereco_ao_pedido():
    end1 = Endereco('08320330', 430)
    end2 = Endereco('04546042', 300)
    carrinho = Carrinho()
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    pedido = Pedido(carrinho,pessoa1)

    pedido.endereco_entrega = copy.deepcopy(end1) 
    pedido.endereco_faturamento = copy.deepcopy(end2)

    assert pedido.endereco_entrega.__str__() == end1.__str__()
    assert pedido.endereco_faturamento.__str__() == end2.__str__()
