from .advanced_calculator_interpreter import AdvancedCalculatorInterpreter


class Access:
    def __init__(self, expression):
        self.expression = expression
        self.interpreter = AdvancedCalculatorInterpreter(expression)

    def interpret(self):
        return self.interpreter.interpret()