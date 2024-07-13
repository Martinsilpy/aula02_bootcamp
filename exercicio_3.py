# Programa para multiplicar dois números
def multiplica(a, b):
    """
    Esta função recebe dois números como entrada e retorna o produto deles.
    """
    return a * b

# Solicita ao usuário que insira o primeiro número
num1 =  float(input("Digite o primeiro número: "))

# Solicita ao usuário que insira o segundo número
num2 =  float(input("Digite o segundo número: "))

# Calcula o produto dos dois números usando a função multiplica
resultado = multiplica(num1, num2)

# Exibe o resultado da multiplicação
print(f"O produto de {num1} e {num2} é {resultado}")