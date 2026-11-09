from __future__ import annotations
from geco_token import Token
from typing import Protocol
from abc import ABC, abstractmethod


class Expr(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def accept(self, visitor: Visitor) -> object:
        pass


class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr):
        self.left = left
        self.op = operator
        self.right = right

    def accept(self, visitor: Visitor):
        return visitor.visitBinary(self)


class Grouping(Expr):
    def __init__(self, expression: Expr):
        self.expression = expression

    def accept(self, visitor: Visitor):
        return visitor.visitGrouping(self)


class Literal(Expr):
    def __init__(self, value: object):
        self.value = value

    def accept(self, visitor: Visitor):
        return visitor.visitLiteral(self)


class Unary(Expr):
    def __init__(self, operator: Token, right: Expr):
        self.op = operator
        self.right = right

    def accept(self, visitor: Visitor):
        return visitor.visitUnary(self)

class Variable(Expr):
    def __init__(self, name):
        self.name = name

    def accept(self, visitor: Visitor) -> object:
        return visitor.visitVariableExpr(self)

class Assign(Expr):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor):
        return visitor.visitAssign(self)


class Visitor(Protocol):
    def visitBinary(self, binary: Binary) -> object:
        pass

    def visitGrouping(self, grouping: Grouping) -> object:
        pass

    def visitLiteral(self, literal: Literal) -> object:
        pass

    def visitUnary(self, unary: Unary) -> object:
        pass

    def visitVariableExpr(self, variable) -> object:
        pass

    def visitAssign(self, expr):
        pass
