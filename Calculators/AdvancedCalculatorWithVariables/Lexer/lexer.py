from Calculators.AdvancedCalculatorWithVariables.Tokens.token_types import TokenTypes
from Calculators.AdvancedCalculatorWithVariables.Tokens.tokens import Token


class Lexer:
    def __init__(self):
        self.list_equation = []
        self.tokens = []

    def tokenize(self, equation):
        self.list_equation = list(equation)
        while len(self.list_equation) > 0:
            c = self.list_equation.pop(0)
            if c in ' \t':
                continue
            elif c in '0123456789':
                number = c
                while len(self.list_equation) > 0 and self.list_equation[0] in '0123456789.':
                    number += self.list_equation.pop(0)
                self.tokens.append(Token(TokenTypes.NUMBER, float(number)))
            elif c in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if c == 'e':
                    self.tokens.append(Token(TokenTypes.E))
                else:
                    self.special_operations(c.lower())
            elif c == ',':
                self.tokens.append(Token(TokenTypes.COMMA))
                if len(self.list_equation) > 0 and self.list_equation[0] == ')':
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
            elif c == '=':
                if self.list_equation[0] == '=':
                    self.list_equation.pop(0)
                    self.tokens.append(Token(TokenTypes.EQUALS))
                elif self.list_equation[0] == '>':
                    self.list_equation.pop(0)
                    self.tokens.append(Token(TokenTypes.GREATER_THAN_OR_EQUAL))
                elif self.list_equation[0] == '<':
                    self.list_equation.pop(0)
                    self.tokens.append(Token(TokenTypes.LESS_THAN_OR_EQUAL))
                elif self.list_equation[0] == '!':
                    self.list_equation.pop(0)
                    self.tokens.append(Token(TokenTypes.NOT_EQUAL))
                else:
                    self.tokens.append(Token(TokenTypes.ASSIGN))
            elif c == '>':
                if self.list_equation[0] == '=':
                    self.list_equation.pop(0)
                    self.tokens.append(Token(TokenTypes.GREATER_THAN_OR_EQUAL))
                else:
                    self.tokens.append(Token(TokenTypes.GREATER_THAN))
            elif c == '<':
                if self.list_equation[0] == '=':
                    self.list_equation.pop(0)
                    self.tokens.append(Token(TokenTypes.LESS_THAN_OR_EQUAL))
                else:
                    self.tokens.append(Token(TokenTypes.LESS_THAN))
            elif c == '!':
                if self.list_equation[0] == '=':
                    self.list_equation.pop(0)
                    self.tokens.append(Token(TokenTypes.NOT_EQUAL))
            else:
                raise ValueError(f'Invalid character: {c}')

    def special_operations(self, c):
        special_operation = c.lower()
        while len(self.list_equation) > 0 and self.list_equation[0].lower() in 'abcdefghijklmnopqrstuvwxyz':
            special_operation += self.list_equation.pop(0).lower()
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
        elif special_operation == 'pi':
            self.tokens.append(Token(TokenTypes.PI))
        elif special_operation == 'rads':
            self.tokens.append(Token(TokenTypes.RADS))
        elif special_operation == 'degrees':
            self.tokens.append(Token(TokenTypes.DEGREES))
        else:
            self.tokens.append(Token(TokenTypes.VARIABLE, special_operation))