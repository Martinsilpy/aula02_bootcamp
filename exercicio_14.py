# Programa para separar e imprimir o dia, o mês e o ano de uma data fornecida pelo usuário
def separa_data(data):
    dia, mes, ano = data.split('/')
    return dia, mes, ano

data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = separa_data(data)

print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")
