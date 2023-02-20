import random

OPERATORS = ["+", "-", "*", ":"]


def generate_expression():
    # Definindo a profundidade da expressão (quantidade de níveis de aninhamento)
    depth = random.randint(2, 4)

    # Lista para armazenar a expressão
    expression = []

    # Gerando o primeiro número
    expression.append(str(random.randint(1, 50)))

    # Gerando os próximos números e operadores
    for i in range(depth):
        expression.append(random.choice(OPERATORS))
        expression.append(random.choice(["(", "[", "{"]))
        expression.append(str(random.randint(1, 50)))

    # Fechando os parênteses, colchetes e chaves
    for i in range(depth):
        expression.append(random.choice([")", "]", "}"]))

    # Juntando todos os elementos da lista em uma única string
    expression_string = "".join(expression)

    # Avaliando a expressão
    result = eval(expression_string)

    # Se o resultado não for um número inteiro, gera uma nova expressão
    if not isinstance(result, int):
        return generate_expression()

    # Retornando a expressão como string
    return expression_string


# Gerando 10 expressões
for i in range(10):
    print(generate_expression())
