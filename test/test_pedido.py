from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import requests

@pytest.mark.test_ped
def test_cria_pedido():
    pessoa1 = PessoaFisica(nome='Carlos', email='tiago@email.com', cpf = '524.222.452-6')
    carrinho = Carrinho()
    pedido = Pedido(carrinho,pessoa1)
    
    assert carrinho == pedido.carrinho
    assert pessoa1 == pedido.comprador

