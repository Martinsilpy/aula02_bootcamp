# Programa para somar dois números inteiros
def soma_inteiros(a, b):
    """
    Esta função recebe dois números inteiros como entrada e retorna a soma deles.
    """
    return a + b

# Solicita ao usuário que insira o primeiro número inteiro
num1 = int(input("Digite o primeiro número inteiro: "))

# Solicita ao usuário que insira o segundo número inteiro
num2 = int(input("Digite o primeiro número inteiro: "))

# Calcula a soma dos dois números inteiros usando a função soma_inteiros
resultado = soma_inteiros(num1, num2)

# Exibe o resultado da soma
print(f"A soma de {num1} e {num2} é {resultado}")