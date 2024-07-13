# Função para converter Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Digeite a temperatura em Celsius: "))

fahrenheit = celsius_para_fahrenheit(celsius)

print(f"{celsius} graus Celsius é igual a {fahrenheit} graus Fahrenheit")
