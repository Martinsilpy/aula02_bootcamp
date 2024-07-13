# Programa para calcular a área de um círculo
import math

def calcula_area_circulo(raio):
    return math.pi * (raio ** 2)

raio = float(input("Digite o raio do círculo: "))

area = calcula_area_circulo(raio)

print(f"A área do círculo com raio {raio} é {area}")