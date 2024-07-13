# Programa para avaliar a operação OR entre duas expressões booleanas
def avalia_or(expr1, expr2):    
    return expr1 or expr2

expr1 = input("Digite a primeira expressão booleana (True/False): ")

expr2 = input("Digite a segunda expressão booleana (True/False): ")

expr1 = True if expr1.lower() == 'true' else False
expr2 = True if expr2.lower() == 'true' else False

resultado = avalia_or(expr1, expr2)

print(f"O resultado da operação OR entre {expr1} e {expr2} é {resultado}")