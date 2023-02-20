import random

def generate_expression():
    """
    Gera uma expressão numérica aleatória com parênteses, colchetes e chaves,
    com resultados inteiros.
    """
    operators = ['+', '-', '*', '/']
    depth = random.randint(1, 3) # profundidade da expressão
    return generate_expression_rec(1, depth, operators)

def generate_expression_rec(curr_depth, max_depth, operators):
    """
    Função auxiliar para gerar a expressão numérica aleatória com parênteses, 
    colchetes e chaves, com resultados inteiros.
    """
    expression = ''
    if curr_depth == max_depth:
        return str(random.randint(0, 10)) # número aleatório inteiro
    else:
        if curr_depth == 1:
            # se estamos no primeiro nível da expressão, adicionamos um parêntese 
            # e escolhemos aleatoriamente um operador
            expression += '('
            expression += generate_expression_rec(curr_depth+1, max_depth, operators)
            expression += ')'
            expression += operators[random.randint(0, len(operators)-1)]
            expression += generate_expression_rec(curr_depth+1, max_depth, operators)
        else:
            # adicionamos aleatoriamente um parêntese, colchete ou chave 
            # e escolhemos aleatoriamente um operador
            bracket_types = ['(', ')', '[', ']', '{', '}']
            expression += bracket_types[random.randint(0, len(bracket_types)-1)]
            expression += generate_expression_rec(curr_depth+1, max_depth, operators)
            expression += bracket_types[random.randint(0, len(bracket_types)-1)]
            expression += operators[random.randint(0, len(operators)-1)]
            expression += generate_expression_rec(curr_depth+1, max_depth, operators)
    return expression

# Teste: gera 10 expressões aleatórias
for i in range(10):
    print(generate_expression())
