from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import requests

@pytest.mark.test_prod
def test_cria_produto():
    prod1 = Produto("0010342967", "Sabonete")
    assert "0010342967" == prod1.id
    assert "Sabonete" == prod1.nome