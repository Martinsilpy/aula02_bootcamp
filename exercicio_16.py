# Programa para avaliar a operação AND entre duas expressões booleanas
def avalia_and(expr1, expr2):
    return expr1 and expr2

expr1 = input("Digite a primeira expressão booleana (True/False): ")

expr2 = input("Digite a segunda expressão booleana (True/False): ")

expr1 = True if expr1 == 'True' else False
expr2 = True if expr2 == 'True' else False

resultado = avalia_and(expr1, expr2)

print(f"O resultado da operação AND entre {expr1} e {expr2} é {resultado}")


