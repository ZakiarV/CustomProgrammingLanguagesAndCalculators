from ..Tokens.token_types import TokenTypes
from .nodes import BinaryExpression, Number


class Parser:
    def __init__(self):
        self.tokens = None
        self.ast = []

    def parse(self, tokens):
        self.tokens = tokens
        self.ast = self.expression()
        return self.ast

    def expression(self):
        return self.addition_subtraction()

    def addition_subtraction(self):
        left = self.multiplication_division()
        while len(self.tokens) > 0 and self.tokens[0].type in (TokenTypes.PLUS, TokenTypes.MINUS):
            token = self.tokens.pop(0)
            right = self.multiplication_division()
            left = BinaryExpression(left, token, right)
        return left

    def multiplication_division(self):
        left = self.number()
        while len(self.tokens) > 0 and self.tokens[0].type in (TokenTypes.MULTIPLY,
                                                               TokenTypes.DIVIDE,
                                                               TokenTypes.EXPONENT):
            token = self.tokens.pop(0)
            right = self.number()
            left = BinaryExpression(left, token, right)
        return left

    def number(self):
        token = self.tokens.pop(0)
        if token.type == TokenTypes.NUMBER:
            return Number(token.value)
        elif token.type == TokenTypes.LPAREN:
            node = self.expression()
            self.tokens.pop(0)
            return node
        else:
            raise ValueError(f'Invalid token: {token}')
