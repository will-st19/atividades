import random

# Definir caracteres de colchetes, parênteses e chaves
BRACKETS = [("(", ")"), ("[", "]"), ("{", "}")]

# Definir operadores matemáticos
OPERATORS = ["+", "-", "*", ":", "÷"]

# Definir intervalos de valores para cada operando
INTERVALS = [(1, 20), (1, 20), (1, 20), (1, 10), (2, 10)]


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
        expression_string = (
            f"{bracket}{operand1} {operator} {operand2}{closing_bracket}"
        )
        result = eval(simplify_expression(expression_string.replace("÷", "/")))
    # Retornar a expressão como uma string
    return expression_string


def simplify_expression(expression_string):
    # Se a expressão tem apenas um caractere e é uma chave, não precisa simplificar
    if (
        len(expression_string) == 3
        and expression_string[0] == "{"
        and expression_string[2] == "}"
    ):
        return expression_string

    # Remove espaços em branco da expressão
    expression_string = expression_string.replace(" ", "")

    # Aplica a simplificação recursivamente enquanto for possível
    changed = True
    while changed:
        changed = False
        for opening_bracket, closing_bracket in BRACKETS:
            # Procura o primeiro bloco de parênteses, colchetes ou chaves
            start = expression_string.find(opening_bracket)
            if start != -1:
                # Procura o último caractere correspondente ao bloco
                count = 1
                for end in range(start + 1, len(expression_string)):
                    if expression_string[end] == opening_bracket:
                        count += 1
                    elif expression_string[end] == closing_bracket:
                        count -= 1
                    if count == 0:
                        break

                # Simplifica a expressão dentro do bloco
                simplified = simplify_expression(expression_string[start + 1 : end])
                if simplified != expression_string[start + 1 : end]:
                    # Substitui o bloco pela expressão simplificada
                    expression_string = (
                        expression_string[: start + 1]
                        + simplified
                        + expression_string[end:]
                    )
                    changed = True
                    break
        if not changed:
            break

    return expression_string


# Testar a função gerando 10 expressões aleatórias
for i in range(10):
    print(generate_expression())
