# Exemplo de causa TypeError

# dado = "Michel"
# try:
#     resultado = len(dado)
#     print(resultado)
# except TypeError as e:
#     print(e)
# else:
#     print("Tudo ocorreu bem")
# finally:
#     print("O importante é participar")


# numero = int(input("Digite um número: "))
# if isinstance(numero, int):
#     print("A variável é um inteiro.")
# else:
#     print("A variável não é um inteiro.")


idade = int(input("Digite sua idade: "))
if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Exatamente 18 anos")
else:
    print("Maior de idade")