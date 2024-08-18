from .basic_calculator_interpreter import BasicCalculator


class Access:
    def __init__(self):
        self.calculator = BasicCalculator()
        self.result = None

    def calculate(self, equation):
        self.result = self.calculator.calculate(equation)
        return self.result