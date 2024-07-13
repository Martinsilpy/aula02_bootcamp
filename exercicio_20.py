# Programa para comparar se dois números são diferentes
def verifica_diferenca(num1, num2):
    return num1 != num2

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

resultado = verifica_diferenca(num1, num2)

if resultado:
    print("Os números são diferentes.")

else:
    print("Os números são iguais.")