"""
Faça um Programa que leia 4 notas de alunos e, 
ao final, mostre na tela as notas lidas e a respectiva média.
"""

def mostra_notas(notas: list):
    print(f'As notas inseridas foram: {notas}')


def calcula_media(notas: list) -> float:
    return (sum(notas)/len(notas))

def app():
    lista_notas = []
    index = 1
    while index < 5:
        nota = input(f"Insira a {index}ª nota: ")
        try:
            lista_notas.append(float(nota))
            index += 1
        except ValueError:
            print("Informe um valor válido!")

    mostra_notas(notas=lista_notas)
    media = calcula_media(lista_notas)
    print(f'A média é {media}.')

    

if __name__ == '__main__':
    app()