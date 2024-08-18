from ..Parser.nodes import BinaryExpression, Number
from ..Tokens.token_types import TokenTypes


class Interpreter:
    def __init__(self):
        self.ast = None
        self.result = None

    def interpret(self, ast):
        self.result = self.evaluate(ast)
        return self.result

    def evaluate(self, node):
        if isinstance(node, Number):
            return node.value
        elif isinstance(node, BinaryExpression):
            return self.evaluate_binary_expression(node)

    def evaluate_binary_expression(self, node):
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)
        if node.operator.type == TokenTypes.PLUS:
            return left + right
        elif node.operator.type == TokenTypes.MINUS:
            return left - right
        elif node.operator.type == TokenTypes.MULTIPLY:
            return left * right
        elif node.operator.type == TokenTypes.DIVIDE:
            return left / right
        elif node.operator.type == TokenTypes.EXPONENT:
            return left ** right
        else:
            raise ValueError(f'Invalid operator: {node.operator}')
