from ..Tokens.token_types import TokenTypes
from ..Tokens.tokens import Token


class Lexer:
    def __init__(self, equation):
        self.equation = list(equation)
        self.tokens = []

    def tokenize(self):
        while len(self.equation) > 0:
            c = self.equation.pop(0)
            if c in ' \t':
                continue
            elif c in '0123456789':
                number = c
                while len(self.equation) > 0 and self.equation[0] in '0123456789.':
                    number += self.equation.pop(0)
                self.tokens.append(Token(TokenTypes.NUMBER, float(number)))
            elif c.lower() in 'abcdefghijklmnopqrstuvwxyz':
                self.special_operations(c)
            elif c == ',':
                self.tokens.append(Token(TokenTypes.COMMA))
                if len(self.equation) > 0 and self.equation[0] == ')':
                    self.tokens.append(Token(TokenTypes.NONE, None))
            elif c == '+':
                self.tokens.append(Token(TokenTypes.PLUS))
            elif c == '-':
                self.tokens.append(Token(TokenTypes.MINUS))
            elif c == '*':
                self.tokens.append(Token(TokenTypes.MULTIPLY))
            elif c == '/':
                self.tokens.append(Token(TokenTypes.DIVIDE))
            elif c == '(':
                self.tokens.append(Token(TokenTypes.LPAREN))
            elif c == ')':
                self.tokens.append(Token(TokenTypes.RPAREN))
            elif c == '^':
                self.tokens.append(Token(TokenTypes.EXPONENT))
            else:
                raise ValueError(f'Invalid character: {c}')

    def special_operations(self, c):
        special_operation = c.lower()
        while len(self.equation) > 0 and self.equation[0].lower() in 'abcdefghijklmnopqrstuvwxyz':
            special_operation += self.equation.pop(0).lower()
        if special_operation == 'sin':
            self.tokens.append(Token(TokenTypes.SIN))
        elif special_operation == 'cos':
            self.tokens.append(Token(TokenTypes.COS))
        elif special_operation == 'tan':
            self.tokens.append(Token(TokenTypes.TAN))
        elif special_operation == 'log':
            self.tokens.append(Token(TokenTypes.LOG))
        elif special_operation == 'sec':
            self.tokens.append(Token(TokenTypes.SEC))
        elif special_operation == 'csc':
            self.tokens.append(Token(TokenTypes.CSC))
        elif special_operation == 'cot':
            self.tokens.append(Token(TokenTypes.COT))
        elif special_operation == 'sqrt':
            self.tokens.append(Token(TokenTypes.SQRT))
        elif special_operation == 'ln':
            self.tokens.append(Token(TokenTypes.LN))
        else:
            raise ValueError(f'Invalid special operation: {special_operation}')