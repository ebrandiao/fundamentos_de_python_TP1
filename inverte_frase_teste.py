def invertevalorfrase(frase,n):
    tupla = ()
    comp = int(len(tupla))
    tupla = frase
    print(tupla)

    if (comp % n) == 0:
        tupla_1 = tupla[:n]
        tupla_2 = tupla[n:]
        tupla3 = tupla_2 + tupla_1
    else:
        tupla_1 = tupla[:n]
        tupla_2 = tupla[n:]
        tupla3 = tupla_2 + tupla_1
    return print(f" O resultado da frase é: {tupla3}")

frase = input("Digite uma frase: ")
n = int(input("Digite um valor inteiro: "))
print(invertevalorfrase(frase,n))