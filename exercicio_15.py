# Programa para concatenar duas strings
def concatena_strings(string1, string2):
    return string1 + string2

string1 = input("Digite a primeira string: ")

string2 = input("Digite a segunda string: ")

resultado = concatena_strings(string1, string2)

print(f"A concatenação das duas strings é: {resultado}")