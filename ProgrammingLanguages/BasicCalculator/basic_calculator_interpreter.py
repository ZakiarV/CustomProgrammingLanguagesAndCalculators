import json


from .Parser.parser import Parser
from .Lexer.lexer import Lexer
from .Interpreter.interpreter import Interpreter


class BasicCalculator:
    def __init__(self, equation):
        self.equation = equation
        self.parser = None
        self.lexer = None
        self.interpreter = None
        self.result = None

    def calculate(self):
        self.lexer = Lexer(self.equation)
        self.lexer.tokenize()
        self.parser = Parser(self.lexer.tokens)
        ast = self.parser.parse()
        self.interpreter = Interpreter(ast)
        self.interpreter.interpret()
        self.result = self.interpreter.result
        return self.result
