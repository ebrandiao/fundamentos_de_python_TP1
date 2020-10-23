"""Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o índice do mesmo.
"""

def verificatupla():
    tupla = ("omega", "voyage", "chevette")
    print("Esse código verifica se o elemento está na tupla.")
    elemento = input("Digite o carro antigo para verificar se está na tupla: ")
    
    if (elemento) in tupla:
        index = tupla.index(elemento)
        print(f"O carro digitado {elemento} está contido na tupla e se índice é {index}")
    else:
        print("o elemento digitado não está na tupla!")
        
verificatupla()