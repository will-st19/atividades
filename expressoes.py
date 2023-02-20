import random

def generate_expression():
    """
    Gera uma expressão numérica aleatória com parênteses, colchetes e chaves,
    com resultados inteiros.
    """
    operators = ['+', '-', '*', '/']
    return generate_expression_rec(0, operators)

def generate_expression_rec(curr_depth, operators):
    """
    Função auxiliar para gerar a expressão numérica aleatória com parênteses, 
    colchetes e chaves, com resultados inteiros.
    """
    expression = ''
    if curr_depth == 0:
        # primeiro nível da expressão
        bracket_types = ['(', '{', '[']
        expression += bracket_types[random.randint(0, len(bracket_types)-1)]
        expression += generate_expression_rec(curr_depth+1, operators)
        expression += bracket_types[random.randint(0, len(bracket_types)-1)]
    elif curr_depth == 3:
        # último nível da expressão
        expression += str(random.randint(0, 10))
        expression += curr_bracket(curr_depth)
    else:
        # outros níveis da expressão
        if random.random() < 0.5:
            # escolhe aleatoriamente um parêntese, colchete ou chave 
            expression += curr_bracket(curr_depth)
            expression += generate_expression_rec(curr_depth+1, operators)
            expression += curr_bracket(curr_depth)
        else:
            # escolhe aleatoriamente um operador
            expression += operators[random.randint(0, len(operators)-1)]
            expression += generate_expression_rec(curr_depth, operators)
            expression += operators[random.randint(0, len(operators)-1)]
    return expression

def curr_bracket(depth):
    """
    Retorna o símbolo de parêntese, colchete ou chave correspondente
    ao nível atual da expressão.
    """
    if depth == 1:
        return '('
    elif depth == 2:
        return '{'
    elif depth == 3:
        return '['
    elif depth == 4:
        return ']'
    elif depth == 5:
        return '}'
    elif depth == 6:
        return ')'

# Teste: gera 10 expressões aleatórias
for i in range(10):
    print(generate_expression())
