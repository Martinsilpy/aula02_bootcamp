# Conversão de String para Minúsculas
def converter_para_minusculas(nome):
    return nome.lower()

nome_completo = input("Digite seu nome completo: ")

nome_minusculas = converter_para_minusculas(nome_completo)

print(f"A string em letras minúsculas é: {nome_minusculas}")