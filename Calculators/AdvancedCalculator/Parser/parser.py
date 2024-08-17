from ..Tokens.token_types import TokenTypes
from .nodes import BinaryExpression, Number, SpecialOperation


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.ast = []

    def parse(self):
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
        elif token.type == TokenTypes.NONE:
            return Number(None)
        elif token.type == TokenTypes.LPAREN:
            node = self.expression()
            self.tokens.pop(0)
            return node
        elif token.type in (TokenTypes.LN, TokenTypes.SIN, TokenTypes.COS,
                            TokenTypes.TAN, TokenTypes.COT, TokenTypes.CSC,
                            TokenTypes.SEC):
            self.tokens.pop(0)
            node = [self.expression()]
            self.tokens.pop(0)
            return SpecialOperation(token, node)
        elif token.type in (TokenTypes.LOG, TokenTypes.SQRT):
            arguments = self.get_arguments()
            return SpecialOperation(token, arguments)
        else:
            raise ValueError(f'Invalid token: {token}')

    def get_arguments(self):
        arguments = []
        while self.tokens[0].type != TokenTypes.RPAREN:
            self.tokens.pop(0)
            arguments.append(self.expression())
        self.tokens.pop(0)
        return arguments
