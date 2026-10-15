# type: ignore
import sys
from pathlib import Path
par_dir = Path(__file__).resolve().parent
print(par_dir)
target = par_dir / "../../src/geco"

sys.path.insert(0, str(target.resolve()))


import unittest
from ast_printer import AstPrinter 
from token_type import Tipo as t
from printer_tool import *

class TestPrinter(unittest.TestCase):
    def setUp(self) -> None:
        self.printer = AstPrinter()

    def testExprDefault(self):
        expression = Binary(
            Unary(
                Token(t.MENOS, "-", None, 1),
                Literal(123)),
            Token(t.ESTRELLA, "*", None, 1),
            Grouping(
                Literal(45.67)) 
        )
        print = self.printer.print(expression)
        self.assertEqual(print, "(* (- 123) (group 45.67))")

    def testOperators(self):
            operators = [
                (t.NO_IGUAL, "!=", None),
                (t.MAYOR, ">", None),
                (t.MAYOR_IGUAL, ">=", None),
                (t.MENOR, "<", None),
                (t.MENOR_IGUAL, "<=", None),
                (t.MENOS, "-", None),
                (t.MENOS_ASIGNAR, "-=", None),
                (t.MODULO, "%", None),
                (t.MODULO_ASIGNAR, "%=", None),
                (t.MAS, "+", None),
                (t.MAS_ASIGNAR, "+=", None),
                (t.BARRA, "/", None),
                (t.DIV_ASIGNAR, "/=", None),
                (t.ESTRELLA, "*", None),
                (t.ESTRELLA_ASIGNAR, "*=", None),
                (t.ASIGNAR, "=", None),
                (t.IGUAL_IGUAL, "==", None),
                (t.Y, "y", None),
                (t.O, "o", None)
            ]

            for tipo, lexema, literal in operators:
                expression = Binary(
                    Literal(1),
                    Token(tipo, lexema, None, 1),
                    Literal(2))

                print = self.printer.print(expression)
                self.assertEqual(print, f"({lexema} 1 2)")

    def testUnaryNegation(self):
        expression  = Unary(
            Token(t.NEGACION, "!", None, 1),
            Literal(5)
        )
        print = self.printer.print(expression)
        self.assertEqual(print, "(! 5)")

    def testNestedUnary(self):
        expression  = Unary(
            Token(t.MENOS, "-", None, 1),
            Unary(
                Token(t.MENOS, "-", None, 1),
                Literal(1)
            ))
        print = self.printer.print(expression)
        self.assertEqual(print, "(- (- 1))")

    def testNestedGrouping(self):
        expression = Grouping(
            Grouping(
                Literal(1)
            )
        )
        print = self.printer.print(expression)
        self.assertEqual(print, "(group (group 1))")

    def testString(self):
        expression = Literal("hola")
        print = self.printer.print(expression)
        self.assertEqual(print, "hola")

if __name__ == "__main__":
    unittest.main()