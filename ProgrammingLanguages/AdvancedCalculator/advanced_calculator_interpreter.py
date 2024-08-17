from .Parser.parser import Parser
from .Lexer.lexer import Lexer
from .Interpreter.interpreter import Interpreter


class AdvancedCalculatorInterpreter:
    def __init__(self, expression):
        self.lexer = None
        self.parser = None
        self.expression = expression
        self.interpreter = None


    def interpret(self):
        self.lexer = Lexer(self.expression)
        self.lexer.tokenize()
        self.parser = Parser(self.lexer.tokens)
        ast = self.parser.parse()
        self.interpreter = Interpreter(ast)
        self.interpreter.interpret()
        return self.interpreter.result
