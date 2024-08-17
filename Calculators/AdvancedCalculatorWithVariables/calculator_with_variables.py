from .Lexer.lexer import Lexer
from .Parser.parser import Parser
from .Interpreter.interpreter import Interpreter


class AdvancedCalculatorWithVariables:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.interpreter = Interpreter()

    def interpret(self, expression):
        self.lexer.tokenize(expression)
        ast = self.parser.parse(self.lexer.tokens)
        return self.interpreter.interpret(ast)