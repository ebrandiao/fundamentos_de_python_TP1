"""
17. Escreva uma função que receba uma string e um número inteiro x e rotacione a string x posições para a esquerda.
Assuma que a string tem pelo menos x caracteres.
Isto é, utilizando como entradas a string “aeiou” e o inteiro 3, o resultado da sua função deve ser “ouaei”.

"""

def invertevalorfrase():
    tupla = ()
    frase = input("Digite uma frase: ")
    tupla = frase
    print(tupla)

    if (int(len(tupla) % 2) == 0):
        tamanho = int(len(tupla) //2)
        tupla_1 = tupla[:tamanho]
        tupla_2 = tupla[tamanho:]
        tupla3 = tupla_2 + tupla_1
    else:
        tamanho = int(len(tupla) //2)
        tupla_1 = tupla[:tamanho]
        tupla_2 = tupla[tamanho:]
        tupla3 = tupla_2 + tupla_1
    return print(f" O resultado da frase é: {tupla3}")

invertevalorfrase()