from printer_tool import Visitor as printer_visitor
from stmt import Visitor as stmt_visitor
from token_type import Tipo
from RtimeError import RtimeError
from error_handler import ErrorHandler
from environment import Environment


class Interpreter(printer_visitor, stmt_visitor):
    def __init__(self) -> None:
        self.environment = Environment()

    def visitVarStmt(self, stmt):
        value = None
        if stmt.initializer is not None:
            value = self.evaluate(stmt.initializer)

        self.environment.define(stmt.name.lexeme, value)
        return None

    def visitVariableExpr(self, variable):
        return self.environment.get(variable.name)

    def visitAssign(self, expr):
        value = self.evaluate(expr.value)
        self.environment.assign(expr.name, value)

    def visitBlock(self, stmt) -> object:
        self.executeBlock(stmt.statements, Environment(self.environment))
        return None

    def executeBlock(self, statements, environment):
        previous = self.environment
        try:
            self.environment = environment
            for statement in statements:
                self.execute(statement)
        finally:
            self.environment = previous
    
    def visitExpression(self, stmt):
        self.evaluate(stmt.expression)
        return None

    def visitPrint(self, stmt):
        value = self.evaluate(stmt.expression)
        print(self.stringify(value))
        return None

    def visitLiteral(self, literal):
        return literal.value

    def visitGrouping(self, grouping):
        return self.evaluate(grouping.expression)

    def evaluate(self, expr):
        return expr.accept(self)

    def visitUnary(self, unary):
        right = self.evaluate(unary.right)
        match (unary.op.type):
            case Tipo.MENOS:
                self.checkNumberOperand(unary.op, right)
                return -float(right)  # type: ignore
            case Tipo.NEGACION:
                return not self.isTruthy(right)
        return None

    def isTruthy(self, object):
        if object is None:
            return False
        if isinstance(object, bool):
            return bool(object)
        return True

    def visitBinary(self, binary) -> object:
        left = self.evaluate(binary.left)
        right = self.evaluate(binary.right)

        match binary.op.type:
            case Tipo.MAYOR:
                self.checkNumberOperands(binary.op, left, right)
                return float(left) > float(right)  # type: ignore
            case Tipo.MAYOR_IGUAL:
                self.checkNumberOperands(binary.op, left, right)
                return float(left) >= float(right)  # type: ignore
            case Tipo.MENOR:
                self.checkNumberOperands(binary.op, left, right)
                return float(left) < float(right)  # type: ignore
            case Tipo.MENOR_IGUAL:
                self.checkNumberOperands(binary.op, left, right)
                return float(left) <= float(right)  # type: ignore
            case Tipo.NO_IGUAL:
                return not self.isEqual(left, right)
            case Tipo.IGUAL_IGUAL:
                return self.isEqual(left, right)
            case Tipo.MENOS:
                self.checkNumberOperands(binary.op, left, right)
                return float(left) - float(right)  # type: ignore
            case Tipo.MAS:
                if isinstance(left, float) and isinstance(right, float):
                    return float(left) + float(right)
                if isinstance(left, str) and isinstance(right, str):
                    return str(left) + str(right)
                raise RtimeError(
                    binary.op, "Los operandos deben ser dos números o dos cadenas."
                )
            case Tipo.BARRA:
                self.checkNumberOperands(binary.op, left, right)
                return float(left) / float(right)  # type: ignore
            case Tipo.ESTRELLA:
                self.checkNumberOperands(binary.op, left, right)
                return float(left) * float(right)  # type: ignore
            case Tipo.MODULO:
                self.checkNumberOperands(binary.op, left, right)
                return float(left) % float(right) # type: ignore

        return None

    def isEqual(self, a, b):
        if a is None and b is None:
            return True
        if a is None:
            return False
        return a == b

    def checkNumberOperand(self, operator, operand):
        if isinstance(operand, float):
            return
        raise RtimeError(operator, "El operando debe ser un número.")

    def checkNumberOperands(self, operator, left, right):
        if isinstance(left, float) and isinstance(right, float):
            return
        raise RtimeError(operator, "Los operandos deben ser números.")

    def interpret(self, statements):
        try:
            for statement in statements:
                self.execute(statement)
        except RtimeError as error:
            ErrorHandler.runtimeError(error)

    def execute(self, stmt):
        stmt.accept(self)

    def stringify(self, object):
        if object is None:
            return "nulo"
        if isinstance(object, float):
            text = str(object)
            if text.endswith(".0"):
                text = text[0 : len(text) - 2]
            return text
        return str(object)
