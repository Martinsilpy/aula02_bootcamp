# Programa de Conversão de Tipo com Validação
def converte_para_inteiro(valor):
    """
    Esta função tenta converter um valor para inteiro.
    """
    try:
        return int(valor)
    except ValueError:
        return "Erro: Não foi possível converter para inteiro."

def converte_para_float(valor):
    """
    Esta função tenta converter um valor para ponto flutuante.
    """
    try:
        return float(valor)
    except ValueError:
        return "Erro: Não foi possível converter para ponto flutuante."

def converte_para_string(valor):
    """
    Esta função converte um valor para string.
    """
    return str(valor)

def main():
    while True:
        try:
            # Solicita ao usuário que insira um valor
            entrada = input("Digite um valor para converter (ou 'Q' para sair): ")

            if entrada.upper() == 'Q':
                print("Saindo do programa...")
                break

            # Converte o valor para os diferentes tipos
            valor_inteiro = converte_para_inteiro(entrada)
            valor_float = converte_para_float(entrada)
            valor_string = converte_para_string(entrada)

            # Exibe os resultados das conversões
            print(f"Valor original: {entrada}")
            print(f"Convertido para inteiro: {valor_inteiro}")
            print(f"Convertido para ponto flutuante: {valor_float}")
            print(f"Convertido para string: {valor_string}")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()
