# Programa para realizar a divisão inteira de dois números
def divisao_inteira(a, b):
    """
    Esta funcao recebe dois números inteiros como entrada e retorna o resultado da divisão
    """
    return a // b

# Solicita ao usuário que insira o primeiro número inteiro
num1 = int(input("Digite o primeiro número inteiro: "))

# Solicita ao usuário que insira o segundo número inteiro
num2 = int(input("Digite o segundo número inteiro: "))

# Calcula a divisão inteira dos dois números usando a função divisão_inteira
resultado = divisao_inteira(num1, num2)

# Exibe o resultado da divisão inteira
print(f"A divisão inteira de {num1} por {num2} é {resultado}")