class BinaryExpression:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f'BinaryExpression({self.left} {self.operator} {self.right})'


class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Number({self.value})'
