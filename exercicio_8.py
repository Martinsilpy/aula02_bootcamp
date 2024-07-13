# Programa para calcular a potência de um número
def calcula_potencia(base, expoente):
    return base ** expoente

base = float(input("Digite a base: "))

expoente = float(input("Digite o expoente: "))

resultado = calcula_potencia(base, expoente)

print(f"{base} elevado a {expoente} é {resultado}")
