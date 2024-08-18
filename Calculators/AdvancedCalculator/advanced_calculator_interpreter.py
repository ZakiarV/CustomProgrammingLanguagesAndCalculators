from .Parser.parser import Parser
from .Lexer.lexer import Lexer
from .Interpreter.interpreter import Interpreter


class AdvancedCalculatorInterpreter:
    def __init__(self):
        self.lexer = Lexer()
        self.parser = Parser()
        self.interpreter = Interpreter()

    def calculate(self, equation):
        self.lexer.tokenize(equation)
        ast = self.parser.parse(self.lexer.tokens)
        return self.interpreter.interpret(ast)
