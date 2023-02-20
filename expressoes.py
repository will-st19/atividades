import random

# Definir caracteres de colchetes, parênteses e chaves
BRACKETS = [("(", ")"), ("[", "]"), ("{", "}")]

# Definir operadores matemáticos
OPERATORS = ["+", "-", "*", ":", "÷"]

# Definir intervalos de valores para cada operando
INTERVALS = [
    (1, 20),
    (1, 20),
    (1, 20),
    (1, 10),
    (2, 10)
]

# Função para gerar uma expressão matemática aleatória
def generate_expression():
    # Escolher um caractere de abertura aleatório
    bracket = random.choice("([{")
    # Escolher um índice aleatório para o caractere de abertura escolhido
    opening_bracket_index = [b[0] for b in BRACKETS].index(bracket)
    # Obter o caractere de fechamento correspondente
    closing_bracket = BRACKETS[opening_bracket_index][1]
    # Escolher um operador matemático aleatório
    operator = random.choice(OPERATORS)
    # Escolher aleatoriamente dois números inteiros no intervalo especificado
    operand1 = random.randint(*INTERVALS[0])
    operand2 = random.randint(*INTERVALS[1])
    # Concatenar a expressão como uma string
    expression_string = f"{bracket}{operand1} {operator} {operand2}{closing_bracket}"
    # Avaliar a expressão e garantir que o resultado é um número inteiro
    result = eval(expression_string)
    while not isinstance(result, int):
        operand1 = random.randint(*INTERVALS[0])
        operand2 = random.randint(*INTERVALS[1])
        expression_string = f"{bracket}{operand1} {operator} {operand2}{closing_bracket}"
        result = eval(expression_string)
    # Retornar a expressão como uma string
    return expression_string

# Testar a função gerando 10 expressões aleatórias
for i in range(10):
    print(generate_expression())
