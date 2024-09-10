import math

from Calculators.AdvancedCalculatorWithVariables.Parser.nodes import (BinaryExpression, Number, SpecialOperation,
                                                                      ComparisonNode, AssignmentNode, VariableNode)
from Calculators.AdvancedCalculatorWithVariables.Tokens.token_types import TokenTypes
from .environment import Environment


class Interpreter:
    def __init__(self):
        self.ast = None
        self.result = None
        self.environment = Environment()

    def interpret(self, ast):
        self.ast = ast
        self.result = self.evaluate(self.ast)
        return self.result

    def evaluate(self, node):
        if isinstance(node, Number):
            return node.value
        elif isinstance(node, BinaryExpression):
            return self.evaluate_binary_expression(node)
        elif isinstance(node, SpecialOperation):
            return self.evaluate_special_operation(node)
        elif isinstance(node, ComparisonNode):
            return self.evaluate_comparison(node)
        elif isinstance(node, AssignmentNode):
            return self.evaluate_assignment(node)
        elif isinstance(node, VariableNode):
            return self.environment.get(node.variable)

    def evaluate_assignment(self, node):
        variable = node.variable
        value = self.evaluate(node.value)
        self.environment.assign(variable, value)
        return value

    def evaluate_comparison(self, node):
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)
        if node.comparison.type == TokenTypes.EQUALS:
            return left == right
        elif node.comparison.type == TokenTypes.NOT_EQUAL:
            return left != right
        elif node.comparison.type == TokenTypes.LESS_THAN:
            return left < right
        elif node.comparison.type == TokenTypes.LESS_THAN_OR_EQUAL:
            return left <= right
        elif node.comparison.type == TokenTypes.GREATER_THAN:
            return left > right
        elif node.comparison.type == TokenTypes.GREATER_THAN_OR_EQUAL:
            return left >= right
        else:
            raise ValueError(f'Invalid comparison: {node.comparison}')

    def evaluate_binary_expression(self, node):
        left = self.evaluate(node.left)
        right = self.evaluate(node.right)
        if node.operator.type == TokenTypes.PLUS:
            return left + right
        elif node.operator.type == TokenTypes.MINUS:
            return left - right
        elif node.operator.type == TokenTypes.MULTIPLY:
            return left * right
        elif node.operator.type == TokenTypes.DIVIDE:
            return left / right
        elif node.operator.type == TokenTypes.EXPONENT:
            return left ** right
        else:
            raise ValueError(f'Invalid operator: {node.operator}')

    def evaluate_special_operation(self, node):
        if node.operation.type == TokenTypes.COS:
            return math.cos(self.evaluate(node.arguments[0]) if node.arguments[1].type == TokenTypes.RADS else math.radians(self.evaluate(node.arguments[0])))
        elif node.operation.type == TokenTypes.SIN:
            return math.sin(self.evaluate(node.arguments[0]) if node.arguments[1].type == TokenTypes.RADS else math.radians(self.evaluate(node.arguments[0])))
        elif node.operation.type == TokenTypes.TAN:
            return math.tan(self.evaluate(node.arguments[0]) if node.arguments[1].type == TokenTypes.RADS else math.radians(self.evaluate(node.arguments[0])))
        elif node.operation.type == TokenTypes.LOG:
            if len(node.arguments) > 1:
                if node.arguments[1].value is not None:
                    return math.log(self.evaluate(node.arguments[0]), self.evaluate(node.arguments[1]))
                else:
                    return math.log(self.evaluate(node.arguments[0]), self.evaluate(node.arguments[1]))
            else:
                return math.log(self.evaluate(node.arguments[0]), 10)
        elif node.operation.type == TokenTypes.SEC:
            return 1 / math.cos(self.evaluate(node.arguments[0]) if node.arguments[1].type == TokenTypes.RADS else math.radians(self.evaluate(node.arguments[0])))
        elif node.operation.type == TokenTypes.CSC:
            return 1 / math.sin(self.evaluate(node.arguments[0]) if node.arguments[1].type == TokenTypes.RADS else math.radians(self.evaluate(node.arguments[0])))
        elif node.operation.type == TokenTypes.COT:
            return 1 / math.tan(self.evaluate(node.arguments[0]) if node.arguments[1].type == TokenTypes.RADS else math.radians(self.evaluate(node.arguments[0])))
        elif node.operation.type == TokenTypes.SQRT:
            if len(node.arguments) > 1:
                if node.arguments[1].value is not None:
                    return math.pow(self.evaluate(node.arguments[0]), 1 / self.evaluate(node.arguments[1]))
                else:
                    return math.pow(self.evaluate(node.arguments[0]), 1 / self.evaluate(node.arguments[1]))
            else:
                return math.sqrt(self.evaluate(node.arguments[0]))
        elif node.operation.type == TokenTypes.LN:
            return math.log(self.evaluate(node.arguments[0]), math.e)
        else:
            raise ValueError(f'Invalid operation: {node.operation}')
