# Programa para remover espaços em branco no início e no final de uma string
def remove_espacos(texto):
    return texto.strip()

frase = input("Digite uma frase: ")

frase_sem_espacos = remove_espacos(frase)

print(f"A frase sem espaços em branco no ínicio e no final é: {frase_sem_espacos}")

