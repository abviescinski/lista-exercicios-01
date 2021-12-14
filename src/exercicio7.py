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
        self.dia: int = dia
        self.mes: int = mes
        self.ano: int = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}."

    def exibe(self):
        return f"{self.dia}/{self.mes}/{self.ano}."

    def avanca_um(self) -> int:
        self.dia += 1
        if (self.mes in meses_30 and self.dia > 30) or self.dia > 31:
            self.dia = 1
            self.mes += 1
        if self.mes > 12:
            self.mes = 1
            self.ano += 1
        return self.exibe()

    def verifica_data(self):
        if self.mes in meses_30 and (self.dia < 1 or self.dia > 30):
            return f"Informe um dia entre 1 e 30."
        elif self.dia < 1 or self.dia > 31:
            return f"Informe um dia entre 1 e 31."
        if self.mes < 1 or self.mes > 12:
           return f"Informe um mês entre 1 e 12."

#verificar as datas com datetime strptime 

def app(dia, mes, ano):
    data = Datas(dia, mes, ano)
    verifica = data.verifica_data()
    if verifica:
        print(verifica)
        return
    print(f'Data: {data}')
    while True:
        cont = input(
            "Deseja avançar para o dia seguinte? (Caso negativo clique enter).\n")
        if cont:
            data.avanca_um()
        else:
            return


if __name__ == "__main__":
    dia = 2
    mes = 2
    ano = 2
    app(dia, mes, ano)
