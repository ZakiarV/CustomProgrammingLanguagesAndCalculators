import math
from Calculators.AdvancedCalculatorWithVariables.Tokens.token_types import TokenTypes
from Calculators.AdvancedCalculatorWithVariables.Tokens.tokens import Token
from .nodes import BinaryExpression, Number, SpecialOperation, ComparisonNode, AssignmentNode, VariableNode


class Parser:
    def __init__(self):
        self.tokens = []
        self.ast = None

    def parse(self, tokens):
        self.tokens = tokens
        self.ast = self.expression()
        return self.ast

    def expression(self):
        if self.tokens[0].type == TokenTypes.VARIABLE and self.tokens[1].type == TokenTypes.ASSIGN:
            return self.assignment()
        else:
            return AssignmentNode("x", self.addition_subtraction())

    def assignment(self):
        variable = self.tokens.pop(0).value
        self.tokens.pop(0)
        value = self.addition_subtraction()
        return AssignmentNode(variable, value)

    def addition_subtraction(self):
        left = self.multiplication_division()
        while len(self.tokens) > 0 and self.tokens[0].type in (TokenTypes.PLUS, TokenTypes.MINUS,
                                                               TokenTypes.EQUALS,
                                                               TokenTypes.NOT_EQUAL, TokenTypes.LESS_THAN,
                                                               TokenTypes.LESS_THAN_OR_EQUAL, TokenTypes.GREATER_THAN,
                                                               TokenTypes.GREATER_THAN_OR_EQUAL):
            token = self.tokens.pop(0)
            right = self.multiplication_division()
            if token.type in (TokenTypes.EQUALS, TokenTypes.NOT_EQUAL, TokenTypes.LESS_THAN,
                              TokenTypes.LESS_THAN_OR_EQUAL, TokenTypes.GREATER_THAN,
                              TokenTypes.GREATER_THAN_OR_EQUAL):
                left = ComparisonNode(left, token, right)
            else:
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
        elif token.type == TokenTypes.VARIABLE:
            return VariableNode(token.value)
        elif token.type == TokenTypes.NONE:
            return Number(None)
        elif token.type == TokenTypes.PI:
            return Number(math.pi)
        elif token.type == TokenTypes.E:
            return Number(math.e)
        elif token.type == TokenTypes.LPAREN:
            node = self.expression()
            self.tokens.pop(0)
            return node
        elif token.type == TokenTypes.RADS or token.type == TokenTypes.DEGREES:
            return token
        elif token.type in (TokenTypes.LN, TokenTypes.SIN, TokenTypes.COS,
                            TokenTypes.TAN, TokenTypes.COT, TokenTypes.CSC,
                            TokenTypes.SEC):
            arguments = self.get_arguments(token)
            return SpecialOperation(token, arguments)
        elif token.type in (TokenTypes.LOG, TokenTypes.SQRT):
            arguments = self.get_arguments(token)
            return SpecialOperation(token, arguments)
        else:
            raise ValueError(f'Invalid token: {token}')

    def get_arguments(self, special_operation):
        arguments = []
        while self.tokens[0].type != TokenTypes.RPAREN:
            self.tokens.pop(0)
            arguments.append(self.addition_subtraction())
        if len(arguments) < 2 and special_operation.type in (TokenTypes.LN, TokenTypes.SIN, TokenTypes.COS,
                                                             TokenTypes.TAN, TokenTypes.COT, TokenTypes.CSC,
                                                             TokenTypes.SEC):
            arguments.append(Token(TokenTypes.RADS))
        self.tokens.pop(0)
        print(len(arguments))
        return arguments
