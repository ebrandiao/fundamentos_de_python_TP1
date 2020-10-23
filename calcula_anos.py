"""2. Faça uma função em Python que receba do usuário a idade de uma pessoa em
anos, meses e dias e retorne essa idade expressa em dias. Considere que todos os anos têm 365 dias.
"""

def calcula_anos():
    print("Esse programa vai calcular a idade informada e transformar em dias")
    calculoemdias = 0
    anoemdias = 0
    mesesemdias = 0
    
    anos = int(input("Informe a idade em anos: "))
    meses = int(input("Informe agora os meses: "))
    dias = int(input("Informe agora em dias: "))
    
    anoemdias = anos * 365
    mesesemdias = meses * 30
    
    calculoemdias = (dias) + (anoemdias) + (mesesemdias)
    
    print(f"A idade em dias é {calculoemdias}")

calcula_anos()
    
    