"""Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive.
O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.
"""
def numero_impares():
    num = int(input("Informe um número para para calcular os números ímpares de 1 até o número digitado: "))
    soma = 0
    for i in range(1, num):
        if num % 2 == 0:
            break
        else:
            soma = soma + num
    print(f"A soma do número 1 até {num} é igual a: {soma}")

numero_impares()
    