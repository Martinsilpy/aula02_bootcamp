# Programa para calcular a média de dois números flutuantes
def calcula_media(a, b):
    return(a + b) / 2

num1 = float(input("Digite o primeiro número: "))

num2 = float(input("Digite o segundo número: "))

media = calcula_media(num1, num2)

print(f"A média de {num1} e {num2} é {media}")
