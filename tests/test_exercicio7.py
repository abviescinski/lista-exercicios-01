import pytest
from src.exercicio7 import Datas


def test_apresenta_data_corretamente():
    data = Datas(31,12,21)
    data_formatada = data.exibe()
    print(data_formatada)
    assert data_formatada == '31/12/21.'


def test_verifica_data_eh_valida():
    data = Datas(32,2,21)
    msg = data.verifica_data()
    assert msg == "Informe um dia entre 1 e 30."

    data = Datas(32,12,21)
    msg = data.verifica_data()
    assert msg == "Informe um dia entre 1 e 31."

    data = Datas(31,15,21)
    msg = data.verifica_data()
    assert msg == "Informe um mês entre 1 e 12."


def test_verifica_avanca_uma_data():
    data = Datas(1,1,21)
    nova_data = data.avanca_um()
    assert nova_data == "2/1/21."

    data = Datas(30,4,21)
    nova_data = data.avanca_um()
    assert nova_data == "1/5/21."

    data = Datas(31,5,21)
    nova_data = data.avanca_um()
    assert nova_data == "1/6/21."

    data = Datas(31,5,21)
    nova_data = data.avanca_um()
    assert nova_data == "1/6/21."