# Programa para somar dois números flutuantes
def soma_flutuantes(a, b):
    """
    Esta função recebe dois números flutuantes como entrada e retorna a soma deles.
    """
    return a + b

# Solicita ao usuário que insira o primeiro número flutuante
num1 = float(input("Digite o primeiro número flutuante: "))

# Solicita ao usuário que insira o segundo número flutuante
num2 = float(input("Digite o segundo número flutuante: "))

# Calcula a soma dos dois números flutuantes usando a função soma_flutuantes
resultado = soma_flutuantes(num1, num2)

# Exibe o resultado da soma
print(f"A soma de {num1} e {num2} é {resultado}")


