"""
Crie uma classe para representar datas com as seguintes regras:
a. deve ter três atributos: o dia, o mês e o ano; ok
b. deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos;
c. encapsule cada um dos atributos; ok
d. forneça o método __str__ para retornar uma representação da data como string. Considere que a data
deve ser formatada mostrando o dia, o mês e o ano separados por barra (/); ok
e. forneça uma operação para avançar uma data para o dia seguinte. ok
"""
import sys


meses_30 = [2, 4, 6, 9, 11]


class Datas:
    def __init__(self, dia, mes, ano):
        self._dia: int = dia
        self._mes: int = mes
        self._ano: int = ano
        self.verifica_data()

    def __str__(self):
        return f'{self._dia}/{self._mes}/{self._ano}.'

    def avanca_um(self) -> int:
        self._dia += 1
        if (self._mes in meses_30 and self._dia > 30) or self._dia > 31:
            self._dia = 1
            self._mes += 1
        if self._mes > 12:
            self._mes = 1
            self._ano += 1

    def verifica_data(self):

        if self._mes in meses_30 and (self._dia < 1 or self._dia > 30):
            print("Informe um dia entre 1 e 30.")
            sys.exit()
        elif self._dia < 1 or self._dia > 31:
            print("Informe um dia entre 1 e 31.")
            sys.exit()
        if self._mes < 1 or self._mes > 12:
            print("Informe um mês entre 1 e 12.")
            sys.exit()


def app():
    try:
        dia = int(input('Insira o dia: '))
        mes = int(input('Insira o mes: '))
        ano = int(input('Insira o ano: '))
    except ValueError:
        print('Informe um valor válido!')

    data = Datas(dia, mes, ano)

    print(f'Data: {data}')

    while True:
        cont = input(
            "Deseja avançar para o dia seguinte? (Caso negativo clique enter).\n")
        if cont:
            data.avanca_um()
            print(f'Data: {data}')
        else:
            break


if __name__ == "__main__":
    app()
