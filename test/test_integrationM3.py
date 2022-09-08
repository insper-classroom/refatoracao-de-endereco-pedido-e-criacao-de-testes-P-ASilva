from classes.Carrinho import Carrinho
from classes.Endereco import Endereco
from classes.PessoaFisica import PessoaFisica
from classes.Produto import Produto
from classes.Pedido import Pedido
from classes.Pagamentos import Pagamento
import pytest
import requests
import copy

# Vide textes de pedido, carrinho e pagamento - A organização por classes faz mais sentido já que as interações são one-way only.