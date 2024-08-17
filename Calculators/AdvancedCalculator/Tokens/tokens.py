from .token_types import TokenTypes


class Token:
    def __init__(self, _type, value=None):
        self.type = _type
        self.value = value

    def __repr__(self):
        return f'Token({self.type}, {self.value})'
