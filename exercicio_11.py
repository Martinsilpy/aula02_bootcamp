# Conversão de String para Maiúsculas
def converter_para_maiúsculas(texto):
    return texto.upper()

texto = input("Digite uma string: ")

texto_maiúsculas = converter_para_maiúsculas(texto)

print(f"A string em maiúsculas é: {texto_maiúsculas}")