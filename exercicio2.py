"""
Faça um Programa que leia uma string e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
from typing import List


def verificacao(frase: str) -> List:
    consoantes = ["a", "e", "i", "o", "u"] 
    consoantes_frase = []
    for c in frase:
        if c in consoantes:
            consoantes_frase.append(c)
    return consoantes_frase    


def app():
    frase = input("Insira sua frase: ")
    consoantes_frase = verificacao(frase)
    print(f'O total de consoantes inseridas foi de {len(consoantes_frase)} consoantes.')
    print(f'As consoantes inseridas foram: {consoantes_frase}.')


if __name__ == "__main__":
    app()