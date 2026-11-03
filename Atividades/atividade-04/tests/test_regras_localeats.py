#Responsável: Tácio Wurdig
import pytest

from src.regras_localeats import calcular_desconto


def test_pedido_de_150_recebe_desconto_de_15():
 resultado = calcular_desconto(150)
 assert resultado == 15

def test_pedido_abaixo_de_100_nao_recebe_desconto():
 resultado = calcular_desconto(80)
 assert resultado == 0

def test_pedido_de_100_recebe_desconto_de_10():
  resultado = calcular_desconto(100)
  assert resultado == 10

def test_valor_negativo_gera_value_error():
 with pytest.raises(ValueError):
  calcular_desconto(-1)