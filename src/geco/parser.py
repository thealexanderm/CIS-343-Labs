from printer_tool import *
from token_type import Tipo as t
from error_handler import ErrorHandler
from stmt import Print, Expression, Var, Block


class ParseError(RuntimeError):
    pass


class Parser:
    def __init__(self, tokens) -> None:
        self.tokens = tokens
        self.current = 0

    def parse(self):
        statements = []
        while not self.isAtEnd():
            statements.append(self.declaration())
        return statements

    def declaration(self):
        try:
            if self.match([t.SEA]):
                return self.varDeclaration()
            return self.statement()
        except ParseError:
            self.synchronize()
            return None

    def varDeclaration(self):
        name = self.consume(t.IDENTIFICADOR, "Se espera un nombre de variable.")

        initializer = None
        if self.match([t.ASIGNAR]):
            initializer = self.expression()

        self.consume(t.PUNTO_Y_COMA, "Se espera ';' después de la declaración de la variable.")
        return Var(name, initializer)

    def statement(self):
        if self.match([t.IMPRIMIR]):
            return self.printStatement()
        if self.match([t.LLAVE_IZQ]):
            return Block(self.block())
        return self.expressionStatement()

    def block(self):
        statements = []
        while not self.check(t.LLAVE_DER) and not self.isAtEnd():
            statements.append(self.declaration())

        self.consume(t.LLAVE_DER, "Se espera '}' después del bloque.")
        return statements

    def printStatement(self):
        value = self.expression()
        self.consume(t.PUNTO_Y_COMA, "Se espera ';' después del valor.")
        return Print(value)

    def expressionStatement(self):
        expr = self.expression()
        self.consume(t.PUNTO_Y_COMA, "Se espera ';' después del valor.")
        return Expression(expr)
    
    def expression(self):
        return self.assignment()

    def assignment(self):
        expr = self.equality()
        if self.match([t.ASIGNAR]):
            equals = self.previous()
            value = self.assignment()

            if isinstance(expr, Variable):
                name = expr.name
                return Assign(name, value)

            self.error(equals, "Destino de asignación no válido.")
        return expr

    def equality(self):
        expr = self.comparison()
        tokens = [t.NO_IGUAL, t.IGUAL_IGUAL]

        while self.match(tokens):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)

        return expr

    def match(self, types: list):
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def check(self, type):
        if self.isAtEnd():
            return False
        return self.peek().type == type

    def advance(self):
        if not self.isAtEnd():
            self.current += 1
        return self.previous()

    def isAtEnd(self):
        return self.peek().type == t.FIN

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        index = self.current - 1
        return self.tokens[index]

    def comparison(self):
        expr = self.term()
        tokens = [t.MAYOR, t.MAYOR_IGUAL, t.MENOR, t.MENOR_IGUAL]

        while self.match(tokens):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)

        return expr

    def term(self):
        expr = self.factor()
        tokens = [t.MENOS, t.MAS]

        while self.match(tokens):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)

        return expr

    def factor(self):
        expr = self.unary()
        tokens = [
            t.BARRA,
            t.ESTRELLA,
            t.MODULO
        ]
        while self.match(tokens):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)

        return expr

    def unary(self):
        tokens = [t.NEGACION, t.MENOS]
        if self.match(tokens):
            operator = self.previous()
            right = self.unary()
            return Unary(operator, right)
        return self.primary()

    def primary(self):
        if self.match([t.FALSO]):
            return Literal(False)
        if self.match([t.CIERTO]):
            return Literal(True)
        if self.match([t.NULO]):
            return Literal(None)
        if self.match([t.NUMERO, t.CADENA]):
            return Literal(self.previous().literal)
        if self.match([t.PAR_IZQ]):
            expr = self.expression()
            self.consume(t.PAR_DER, "Se esperaba ')' después de la expresión.")
            return Grouping(expr)
        if self.match([t.IDENTIFICADOR]):
            return Variable(self.previous())
        raise self.error(self.peek(), "Se esperaba una expresión.")

    def consume(self, type, message):
        if self.check(type):
            return self.advance()
        raise self.error(self.peek(), message)

    def error(self, token, message):
        ErrorHandler.error(token, message)
        return ParseError()

    def synchronize(self):
        self.advance()

        while not self.isAtEnd():
            if self.previous().type == t.PUNTO_Y_COMA:
                break
            match self.peek().type:
                case t.CLASE:
                    return
                case t.DEFINICION:
                    return
                case t.SEA:
                    return
                case t.DESDE:
                    return
                case t.SI:
                    return
                case t.MIENTRAS:
                    return
                case t.IMPRIMIR:
                    return
                case t.RETORNAR:
                    return

            self.advance()
