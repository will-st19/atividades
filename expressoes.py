import random

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def is_operator(self):
        return self.value in ["+", "-", "*", "/"]

    def evaluate(self):
        if self.is_operator():
            left_value = self.left.evaluate()
            right_value = self.right.evaluate()
            if self.value == "+":
                return left_value + right_value
            elif self.value == "-":
                return left_value - right_value
            elif self.value == "*":
                return left_value * right_value
            elif self.value == "/":
                return left_value / right_value
        else:
            return self.value

    def __repr__(self):
        if self.is_operator():
            return f"({self.left} {self.value} {self.right})"
        else:
            return str(self.value)


def generate_expression(depth):
    if depth == 0:
        # Gerar um número aleatório entre 1 e 10
        return Node(random.randint(1, 10))

    # Escolher um operador aleatório
    operator = random.choice(["+", "-", "*", "/"])

    # Gerar recursivamente a expressão esquerda e a expressão direita
    left_expression = generate_expression(depth - 1)
    right_expression = generate_expression(depth - 1)

    # Retornar um novo nó com o operador e as expressões filhas
    return Node(operator, left=left_expression, right=right_expression)


for i in range(10):
    expression = generate_expression(2)
    print(expression, "=", expression.evaluate())
