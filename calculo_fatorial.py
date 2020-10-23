"""3. Escreva uma função em Python que calcule o fatorial de um dado número N usando um for.
O fatorial de N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1.
Por exemplo, para N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120.
Se N for negativo, exiba uma mensagem indicando que não é possível calcular seu fatorial.
"""

def calculo_fatorial():
    print("Esse programa calcula fatorial de um número fornecido pelo usuário!!")
    num = int(input("Informe um número para calcular a fatorial dele: "))
    fatorial = 1
    for i in range(num):
        if num <= 0:
            print("Não é possível calular seu fatorial")
    
        else:
            fatorial = num * (num - 1)
            
        print(f"O fatorial do número {num} x {num-1} é: {fatorial}")

calculo_fatorial()