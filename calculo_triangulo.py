"""
Escreva um programa em Python que receba três valores reais X, Y e Z, guarde esses valores numa tupla
e verifique se esses valores podem ser os comprimentos dos lados de um triângulo e, neste caso,
retorne qual o tipo de triângulo formado.

Para que X, Y e Z formem um triângulo é necessário que a seguinte propriedade seja satisfeita:
o comprimento de cada lado de um triângulo deve ser menor do que a soma do comprimento dos outros dois lados.
Além disso, o programa deve identificar o tipo de triângulo formado observando as seguintes definições:

Triângulo Equilátero: os comprimentos dos três lados são iguais.
Triângulo Isósceles: os comprimentos de dois lados são iguais.
Triângulo Escaleno: os comprimentos dos três lados são diferentes.
"""
def calculatriangulo(x, y, z):
    tupla = ()
    if x <= 90 and y <= 90 and z <= 90:
        if x == 45 and y == 45 and z == 45:
            print("O triângulo é equilátero!!")
        elif x == 90 and y == 45 and z == 45:
            print("O triângulo é Isóceles!!")
        else:
            print("O triângulo é escaleno!!")
    else:
        print("Os valores informados não correspondem a um triângulo!!")

x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))
z = int(input("Informe o valor de z: "))
print(calculatriangulo(x, y, z ))