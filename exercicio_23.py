# Programa de Calculadora Simples
def soma(a, b):
    """
    Esta função retorna a soma de a e b.
    """
    return a + b

def subtrai(a, b):
    """
    Esta função retorna a subtração de a e b.
    """
    return a - b

def multiplica(a, b):
    """
    Esta função retorna a multiplicação de a e b.
    """
    return a * b

def divide(a, b):
    """
    Esta função retorna a divisão de a por b.
    """
    return a / b

def main():
    while True:
        try:
            # Solicita ao usuário que escolha a operação
            operacao = input("Digite a operação (+, -, *, /) ou 'Q' para sair: ").upper()

            if operacao == 'Q':
                print("Saindo do programa...")
                break

            if operacao not in ['+', '-', '*', '/']:
                print("Operação inválida! Por favor, digite uma operação válida (+, -, *, /) ou 'Q' para sair.")
                continue

            # Solicita ao usuário que insira os dois números
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            # Realiza a operação de acordo com a escolha do usuário
            if operacao == '+':
                resultado = soma(num1, num2)
            elif operacao == '-':
                resultado = subtrai(num1, num2)
            elif operacao == '*':
                resultado = multiplica(num1, num2)
            elif operacao == '/':
                if num2 == 0:
                    print("Erro: Divisão por zero não é permitida.")
                    continue
                resultado = divide(num1, num2)

            print(f"O resultado de {num1} {operacao} {num2} é {resultado}")

        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
