# Programa para inverter um valor booleano
def inverte_booleano(valor):    
    return not valor

valor = input("Digite um valor booleano (True/False): ")

valor_booleano = True if valor.lower() == 'true' else False

valor_invertido = inverte_booleano(valor_booleano)

print(f"O valor booleano invertido de {valor_booleano} é {valor_invertido}")
