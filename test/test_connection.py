from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import requests

@pytest.mark.test_connection
def test_cep_falha_de_conexao():
    with pytest.raises(requests.exceptions.ConnectionError):
        Endereco.consultar_cep('08320330')
