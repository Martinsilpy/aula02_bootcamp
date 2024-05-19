# Programa para realizar a divisão inteira de dois números

try:
    # Solicita ao usuário para inserir o primeiro número inteiro
    numero1 = int(input("Digite o primeiro número inteiro: "))

    # Solicita ao usuário para inserir o segundo número inteiro
    numero2 = int(input("Digite o segundo número inteiro: "))

    # Calcula a divisão inteira dos dois números
    divisao_inteira = numero1 // numero2

    # Exibe o resultado usando f-string
    print(f"A divisão inteira de {numero1} por {numero2} é: {divisao_inteira}")

# Captura e trata a exceção de divisão por zero
except ZeroDivisionError:
    print("Erro: Divisão inteira por zero não é permitida.")

# Captura e trata a exceção de interrupção do teclado (Ctrl+C)
except KeyboardInterrupt:
    print("\nVocê interrompeu a entrada do número. Tente novamente.")

# Captura e trata a exceção de entrada inválida (não é um número inteiro)
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro válido.")
