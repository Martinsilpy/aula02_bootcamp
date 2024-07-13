# Programa para calcular o quadrado de um número
def calcula_quadrado(numero):
    """
    Esta função recebe um número como entrada e retorna o quadrado dele.
    """
    return numero ** 2

# Solicita ao usuário que insira um número
numero = float(input("Digite um número: "))

# Calcula o quadrado do número usando a função calcula_quadrado
quadrado = calcula_quadrado(numero)

# Exibe o resultado do quadrado
print(f"O quadrado de {numero} é {quadrado}")