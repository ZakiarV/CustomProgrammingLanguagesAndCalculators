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