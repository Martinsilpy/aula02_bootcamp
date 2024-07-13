# Programa Verificador de Palíndromo
def verifica_palindromo(texto):
    texto = texto.replace(" ", "").lower()
    return texto == texto[::-1]

def main():
    while True:
        try:
            texto = input("Digite uma palavra ou frase (ou 'Q' para sair): ")

            if texto.upper() == 'Q':
                print("Saindo do programa...")
                break

        
            if verifica_palindromo(texto):
                print(f" '{texto}' é um palíndromo.")
            else:
                print(f" '{texto}' não é um palíndromo.")

        except Exception as e:
            print (f"Ocorreu um erro: {e}")

if __name__=="__main__":
    main()