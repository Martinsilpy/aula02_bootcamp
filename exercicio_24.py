# Programa Classificador de Números
def classifica_numero(num):
    """
    Esta função classifica um número como positivo, negativo ou zero.
    """
    if num > 0:
        return "positivo"
    elif num < 0:
        return "negativo"
    else:
        return "zero"

def main():
    while True:
        try:
            # Solicita ao usuário que insira um número
            entrada = input("Digite um número para classificar (ou 'Q' para sair): ")

            if entrada.upper() == 'Q':
                print("Saindo do programa...")
                break

            # Converte a entrada para um número de ponto flutuante
            num = float(entrada)

            # Classifica o número usando a função classifica_numero
            classificacao = classifica_numero(num)

            # Exibe o resultado da classificação
            print(f"O número {num} é {classificacao}.")

        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
