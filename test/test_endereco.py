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
    end1 = Endereco(int('08320330') , 430)
    end2 = Endereco('08320330' , 430)

    assert '08320330' == end2.cep
    assert 430 == end2.numero