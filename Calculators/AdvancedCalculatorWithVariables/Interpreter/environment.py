class Environment:
    def __init__(self, parent=None):
        self.parent = parent
        self.variables = {}

    def assign(self, variable, value):
        if variable in self.variables:
            self.variables[variable] = value
        elif self.parent:
            self.parent.assign(variable, value)
        else:
            self.define(variable, value)

    def get(self, variable):
        if variable in self.variables:
            return self.variables[variable]
        elif self.parent:
            return self.parent.get(variable)
        else:
            raise ValueError(f'Variable {variable} not found')

    def define(self, variable, value):
        self.variables[variable] = value
