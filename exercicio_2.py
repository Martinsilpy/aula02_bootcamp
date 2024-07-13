# Programa para calcular o resto da divisão por 5
def resto_divisao_por_5(numero):
    """
    Esta função recebe um número e retorna o resto da divisão deste número por 5.
    """
    return numero % 5

# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))

# Calcula o resto da divisão do número por 5 usando a função resto_divisão_por_5
resto = resto_divisao_por_5(numero)

# Exibe o resultado do resto da divisão
print(f"O resto da divisão de {numero} por 5 é {resto}")

