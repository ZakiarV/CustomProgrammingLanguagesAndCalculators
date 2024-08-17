from .calculator_with_variables import AdvancedCalculatorWithVariables


class Access:
    def __init__(self):
        self.calculator = AdvancedCalculatorWithVariables()

    def interpret(self, expression):
        return self.calculator.interpret(expression)