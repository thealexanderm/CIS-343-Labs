from __future__ import annotations
from geco_token import Token
from typing import Protocol

class Expr:
    def __init__(self) -> None:
        pass
    def accept(self, visitor:Visitor):
        pass

class Binary(Expr):
    def __init__(self, left:Expr, operator:Token, right: Expr) -> None:
        self.left = left
        self.op = operator
        self.right = right

    def accept(self, visitor: Visitor):
        visitor.visitBinary(self)

class Grouping(Expr):
    def __init__(self, expression: Expr) -> None:
        self.expression = expression

    def accept(self, visitor: Visitor):
        visitor.visitGrouping(self)
        
class Literal(Expr):
    def __init__(self, value:object) -> None:
        self.value = value

    def accept(self, visitor: Visitor):
        visitor.visitLiteral(self)

class Unary(Expr):
    def __init__(self, operator:Token, right:Expr) -> None:
        self.op = operator
        self.right = right

    def accept(self, visitor: Visitor):
        visitor.visitUnary(self)

class Visitor(Protocol):
    def visitBinary(self, binary:Binary):
        pass
    def visitGrouping(self, grouping:Grouping):
        pass
    def visitLiteral(self, literal:Literal):
        pass
    def visitUnary(self, unary:Unary):
        pass