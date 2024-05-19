# Programa para separar e imprimir o dia, o mês e o ano de uma data fornecida pelo usuário

# Solicita ao usuário para inserir uma data no formato "dd/mm/aaaa"
data = input("Digite uma data no formato dd/mm/aaaa: ")

# Separa a data em dia, mês e ano
dia, mes, ano = data.split('/')

# Exibe o resultado usando f-string
print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")
