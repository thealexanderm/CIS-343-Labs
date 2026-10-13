from __future__ import annotations
from token_type import Tipo as t
from printer_tool import *

class AstPrinter(Visitor):
    def print(self, expr:Expr):
        return expr.accept(self)
    
    def visitBinary(self, binary: Binary):
        return self.parenthesize(binary.op.lexeme, binary.left, binary.right)

    def visitGrouping(self, grouping: Grouping):
        return self.parenthesize("group", grouping.expression)

    def visitLiteral(self, literal: Literal):
        if (literal.value is None): 
            return "nulo"
        return literal.value

    def visitUnary(self, unary: Unary):
        return self.parenthesize(unary.op.lexeme, unary.right)

    def parenthesize(self, name:str, *exprs: Expr):
        builder = ""
        builder+=f"({name}"
        for  expr in exprs:
            builder += " "
            builder += str(expr.accept(self))

        builder += ")"

        return builder

if __name__ == "__main__":
    expression = Binary(
        Unary(
            Token(t.MENOS, "-", None, 1),
            Literal(123)),
        Token(t.ESTRELLA, "*", None, 1),
        Grouping(
            Literal(45.67)) 
    )

    print(AstPrinter().print(expression))