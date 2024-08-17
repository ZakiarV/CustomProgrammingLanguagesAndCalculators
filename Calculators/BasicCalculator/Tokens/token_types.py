from enum import Enum


class TokenTypes(Enum):
    NUMBER = 1
    PLUS = 2
    MINUS = 3
    MULTIPLY = 4
    DIVIDE = 5
    EXPONENT = 6
    LPAREN = 7
    RPAREN = 8
    EOF = 9
