# Programa para comparar se dois números são iguais
def compara_numeros(num1, num2):
    return num1 == num2

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

resultado = compara_numeros(num1, num2)

if resultado:
    print("Os números são iguais.")

else:
    print("Os números são diferentes.")
