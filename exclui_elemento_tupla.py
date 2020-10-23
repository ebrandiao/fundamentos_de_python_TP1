"""Dada uma tupla e um elemento, elimine esse elemento da tupla.
"""


def eliminaelementodatupla():
    tupla = ()
    criatupla = input("Digite os elementos para criar sua tupla: ")
    tupla = criatupla
    print(tupla)
    excluielemento = input("Digite o nome do elemento que deseja excluir: ")
    if (excluielemento) in tupla:
        lista1 = list(tupla)
        lista1.remove(excluielemento)
        tupla = tuple(lista1)
        print(tupla)
    else:
        print("o elemento digitado não está na tupla!")
      
eliminaelementodatupla()