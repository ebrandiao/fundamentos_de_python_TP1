def calculo_fatorial():
    print("Esse programa calcula fatorial de um número fornecido pelo usuário!!")
    num = int(input("Informe um número para calcular a fatorial dele: "))
    fatorial = 1
    # while True:
    for i in range(num):
        if num <= 0:
            print("Não é possível calular seu fatorial")
        
        else:
            fatorial = num * (num - 1)
            print(f"O fatorial do número {num} x {num-1} é: {fatorial}")

calculo_fatorial()