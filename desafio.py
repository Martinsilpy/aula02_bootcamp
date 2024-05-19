# Programa para validar e processar nome, salário e bônus do usuário

# Bloco para validação do nome do usuário
try:
    # Solicita ao usuário para inserir o nome
    nome = input("Digite seu nome: ")

    # Verifica se o nome está vazio
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    
    # Verifica se o nome contém números
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    
    # Se o nome for válido, imprime o nome
    else:
        print("Nome válido:", nome)

# Captura e trata erros relacionados ao nome
except ValueError as e:
    print(e)
    exit()

# Bloco para validação do salário do usuário
try:
    # Solicita ao usuário para inserir o valor do salário
    salario = float(input("Digite o valor do seu salário: "))
    
    # Verifica se o salário é um valor positivo
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
        exit()

# Captura e trata erros de entrada de salário
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()

# Bloco para validação do bônus do usuário
try:
    # Solicita ao usuário para inserir o valor do bônus
    bonus = float(input("Digite o valor do bônus recebido: "))
    
    # Verifica se o bônus é um valor positivo
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bônus.")
        exit()

# Captura e trata erros de entrada de bônus
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

# Cálculo do bônus final recebido pelo usuário
bonus_recebido = 1000 + salario * bonus  # Exemplo simples de KPI

# Exibe o resultado final, mostrando o salário e o bônus formatados
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
