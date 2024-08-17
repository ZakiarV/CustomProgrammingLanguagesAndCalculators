from .basic_calculator_interpreter import BasicCalculator


class Access:
    def __init__(self, equation):
        self.equation = equation
        self.calculator = BasicCalculator(self.equation)
        self.result = None

    def calculate(self):
        self.result = self.calculator.calculate()
        return self.result