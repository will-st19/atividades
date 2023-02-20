import sympy
import random


class Node:
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator

    def evaluate(self):
        left_val = self.left.evaluate() if isinstance(self.left, Node) else self.left
        right_val = (
            self.right.evaluate() if isinstance(self.right, Node) else self.right
        )

        if self.operator == "+":
            return left_val + right_val
        elif self.operator == "-":
            return left_val - right_val
        elif self.operator == "*":
            return left_val * right_val
        elif self.operator == "/" and right_val != 0:
            return left_val / right_val
        else:
            raise ValueError("Operador inválido")

    def __str__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        left = str(self.left) if self.left is not None else ""
        right = str(self.right) if self.right is not None else ""
        op = self.operator if self.operator is not None else ""
        return f"({left} {op} {right})"


def generate_expression(depth):
    if depth == 0:
        return random.randint(1, 10)

    left = generate_expression(depth - 1)
    right = generate_expression(depth - 1)
    operator = random.choice(["+", "-", "*", "/"])

    return Node(left, right, operator)


# for i in range(5):
#     expression = generate_expression(depth=2)
#     print(expression, "=", expression.evaluate())

for i in range(5):
    while True:
        expression = generate_expression(depth=3)
        result = expression.evaluate()
        if isinstance(result, int) and result >= 0:
            break
    print(expression, "=", result)
