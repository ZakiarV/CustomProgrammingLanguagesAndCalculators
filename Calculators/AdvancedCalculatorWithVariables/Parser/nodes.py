class BinaryExpression:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __repr__(self):
        return f'BinaryExpression({self.left} {self.operator} {self.right})'


class SpecialOperation:
    def __init__(self, operation, arguments):
        self.operation = operation
        self.arguments = arguments

    def __repr__(self):
        return f'SpecialOperation({self.operation}({self.arguments}))'


class Number:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Number({self.value})'


class AssignmentNode:
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __repr__(self):
        return f'AssignmentNode({self.variable} = {self.value})'


class VariableNode:
    def __init__(self, variable):
        self.variable = variable

    def __repr__(self):
        return f'VariableNode({self.variable})'


class ComparisonNode:
    def __init__(self, left, comparison, right):
        self.left = left
        self.comparison = comparison
        self.right = right

    def __repr__(self):
        return f'EqualsNode({self.left} {self.comparison} {self.right})'
