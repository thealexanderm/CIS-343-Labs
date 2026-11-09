from RtimeError import RtimeError

class Environment:
    def __init__(self, enclosing=None) -> None:
        self.values: dict[str, object] = {}
        self.enclosing = enclosing

    def define(self, name, value):
        self.values[name] = value

    def get(self, name):
        if name.lexeme in self.values:
            return self.values[name.lexeme]

        if self.enclosing is not None:
            return self.enclosing.get(name)
        
        raise RtimeError(name, f"Variable no definida '{name.lexeme}'.")

    def assign(self, name, value):
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
            return

        if self.enclosing is not None:
            self.enclosing.assign(name, value)
            return
        
        raise RtimeError(name, f"Variable no definida '{name.lexeme}'.")