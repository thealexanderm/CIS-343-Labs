from __future__ import annotations
from geco_token import Token
from typing import Protocol
from abc import ABC, abstractmethod

class Expr(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def accept(self, visitor:Visitor):
        pass

class Binary(Expr):
    def __init__(self, left:Expr, operator:Token, right: Expr):
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
    def __init__(self, value:object):
        self.value = value

    def accept(self, visitor: Visitor):
        return visitor.visitLiteral(self)

class Unary(Expr):
    def __init__(self, operator:Token, right:Expr):
        self.op = operator
        self.right = right

    def accept(self, visitor: Visitor):
        return visitor.visitUnary(self)

class Visitor(Protocol):
    def visitBinary(self, binary:Binary):
        pass
    def visitGrouping(self, grouping:Grouping):
        pass
    def visitLiteral(self, literal:Literal):
        pass
    def visitUnary(self, unary:Unary):
        pass