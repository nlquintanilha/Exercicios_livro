
def calcular preco_custo_atacado(preco_capa, desconto_livraria, transporte_primeiro, transporte_adicional, quantidade):
    """
    Calcula o custo total de atacado de livros considerando o preço de capa, desconto da livraria,
    custo de transporte do primeiro livro e custo adicional por livro.
    
    Args:
        preco_capa (float): Preço de capa do livro.
        desconto_livraria (float): Desconto da livraria (em decimal).
        transporte_primeiro (float): Custo do transporte do primeiro livro.
        transporte_adicional (float): Custo do transporte adicional por livro.
        quantidade (int): Quantidade de livros.

    Returns:
        tuple: Custo total, preço com desconto, valor do desconto, custo dos livros e custo de transporte.
    """
    if not isinstance(preco_capa, (int, float)) or not isinstance(desconto_livraria, (int, float)) or \


try: 
    preco_capa = 24.95
    desconto_livraria = 0.40 
    transporte_primeiro = 3.00
    trasporte_adicional = 0,75
    quantidade = 60

#validação dos dados de entrada


    if preco_capa <= 0
    raise ValueError("Preço da capa deve ser maior que zero.")

if desconto_livraria < = 0:
    raise ValueError("Desconto deveestar entre 0 e 1.")

if quantidade <= 0: 
    raise ValueError("Quantidade deve ser maior que zero.")

if transporte_primeiro < 0 or transporte_adicional < 0:
    raise ValueError("Custo de transporte não podem ser negativos.")

#1. calcular preços com desconto por livro

try:
    preco_com_desconto = preco_capa * (1 - desconto_livraria)
    desconto_valor = preco_capa * desconto_livraria
except Exception as e:
        raise ValueError("Erro ao calcular o preço com desconto. Verifique os valores de entrada ")

#2. calcular custo total de livros 

try:
     custo_livros = preco_com_desconto * quantidade
except Exception as e:
        raise ValueError("Erro ao calcular o custo dos livros. Verifique os valores de entrada.")

#3. calcular custo de transporte
   try:
     exemplares_adicionais = quantidade - 1
     if exemplares_adicionais < 0:
         exemplares_adicionais = 0

     custo_transporte = transporte_primeiro + (exemplares_adicionais * transporte_adicional)
   except Exception as e:
        raise ValueError("Erro ao calcular o custo de transporte. Verifique os valores de entrada.")

#4. Calcular custo total de atacado
try:
    custo_total = custo_livros + custo_transporte
except Exception as e:
        raise ValueError("Erro ao calcular o custo total. Verifique os valores de entrada.")    
    return custo_total, preco_com_desconto, desconto_valor, custo_livros, custo_transporte

def calcular com input usuario():
    try:
        preco_capa = float(input("Digite o preço de capa do livro: "))
        desconto_livraria = float(input("Digite o desconto da livraria (em decimal, por exemplo, 0.40 para 40%): "))
        transporte_primeiro = float(input("Digite o custo do transporte do primeiro livro: "))
        transporte_adicional = float(input("Digite o custo do transporte adicional por livro: "))
        quantidade = int(input("Digite a quantidade de livros: "))

        return calcular_preco_custo_atacado(preco_capa, desconto_livraria, transporte_primeiro, transporte_adicional, quantidade)
    except ValueError as e:
        print(f"Erro: {e}")
        return None

     


