# Programa de Conversor de Temperatura
def celsius_para_fahrenheit(celsius):
    """
    Esta função converte a temperatura de Celsius para Fahrenheit.
    """
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    """
    Esta função converte a temperatura de Fahrenheit para Celsius.
    """
    return (fahrenheit - 32) * 5/9

def main():
    while True:
        try:
            # Solicita ao usuário que escolha o tipo de conversão
            escolha = input("Digite 'C' para converter de Celsius para Fahrenheit ou 'F' para converter de Fahrenheit para Celsius (ou 'Q' para sair): ").upper()

            if escolha == 'Q':
                print("Saindo do programa...")
                break

            if escolha not in ['C', 'F']:
                print("Escolha inválida! Por favor, digite 'C', 'F' ou 'Q'.")
                continue

            # Solicita ao usuário que insira a temperatura a ser convertida
            temperatura = float(input("Digite a temperatura a ser convertida: "))

            # Realiza a conversão de acordo com a escolha do usuário
            if escolha == 'C':
                resultado = celsius_para_fahrenheit(temperatura)
                print(f"{temperatura}°C é igual a {resultado}°F")
            elif escolha == 'F':
                resultado = fahrenheit_para_celsius(temperatura)
                print(f"{temperatura}°F é igual a {resultado}°C")

        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido para a temperatura.")

if __name__ == "__main__":
    main()
