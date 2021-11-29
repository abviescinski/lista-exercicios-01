"""
Crie uma classe para representar datas com as seguintes regras:
a. deve ter três atributos: o dia, o mês e o ano; ok
b. deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos;
c. encapsule cada um dos atributos; ok
d. forneça o método __str__ para retornar uma representação da data como string. Considere que a data
deve ser formatada mostrando o dia, o mês e o ano separados por barra (/); ok
e. forneça uma operação para avançar uma data para o dia seguinte.
"""

class Datas:
    def __init__(self, dia, mes, ano):
        self._dia: int = dia
        self._mes: int = mes
        self._ano: int = ano

    def __str__(self):
        return f'{self._dia}/{self._mes}/{self._ano}.'

    def avanca_um(self) -> int:
        self._dia += 1

    

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
        cont = input("Deseja avançar para o dia seguinte? Caso negativo clique enter.")
        if cont:
            data.avanca_um()
            print(f'Data: {data}')    
        else:
            break        



if __name__ == "__main__":
    app()
     