from .advanced_calculator_interpreter import AdvancedCalculatorInterpreter


class Access:
    def __init__(self):
        self.interpreter = AdvancedCalculatorInterpreter()

    def interpret(self, expression):
        return self.interpreter.calculate(expression)