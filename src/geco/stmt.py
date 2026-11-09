from __future__ import annotations
from geco_token import Token
from typing import Protocol
from abc import ABC, abstractmethod

class Stmt(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def accept(self, visitor):
        pass

class Block(Stmt):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitBlock(self)

class Expression(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitExpression(self)

class Print(Stmt):
    def __init__(self, expression):
        self.expression = expression

    def accept(self, visitor):
        return visitor.visitPrint(self)

class Var(Stmt):
    def __init__(self, name, initializer):
        self.name = name
        self.initializer = initializer

    def accept(self, visitor):
        return visitor.visitVarStmt(self)


class Visitor(Protocol):
    def visitBlock(self, stmt) -> object:
        pass

    def visitClass(self, stmt) -> object:
        pass

    def visitExpression(self, stmt) -> object:
        pass

    def visitFunction(self, stmt) -> object:
        pass

    def visitIf(self, stmt):
        pass

    def visitPrint(self, stmt):
        pass

    def visitReturn(self, stmt):
        pass

    def visitVarStmt(self, stmt):
        pass

    def visitWhile(self, stmt):
        pass