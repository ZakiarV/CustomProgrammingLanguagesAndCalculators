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
    COS = 9
    SIN = 10
    TAN = 11
    LOG = 12
    SEC = 13
    CSC = 14
    COT = 16
    COMMA = 15
    SQRT = 17
    LN = 18
    NONE = 19
    ASSIGN = 20
    VARIABLE = 21
    EQUALS = 22
    LESS_THAN = 23
    GREATER_THAN = 24
    LESS_THAN_OR_EQUAL = 25
    GREATER_THAN_OR_EQUAL = 26
    NOT_EQUAL = 27

