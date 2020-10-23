"""Dada uma tupla, retorne 2 tuplas onde cada uma representa uma metade da tupla original.
"""
def dividetupla():
    tupla = ()
    criatupla = input("Digite 4 elementos para criar sua tupla: ")
    tupla = criatupla
    print(tupla)
    
    if (int(len(tupla) % 2) == 0):
        tamanho = int(len(tupla) //2)
        tupla_1 = tupla[:tamanho]
        tupla_2 = tupla[tamanho:]
    else:
        tamanho = int(len(tupla) //2)
        tupla_1 = tupla[:tamanho]
        tupla_2 = tupla[tamanho:]
    return print(f" O resultado é Tupla_1: {tupla_1} e o resultado da Tupla_2: {tupla_2}")
        
dividetupla()