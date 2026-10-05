import unittest

from token_type import Tipo as t
from scanner import Scanner
from unittest.mock import patch

from pathlib import Path

DIR = Path(__file__).parent

class TestScanner(unittest.TestCase):
    def assert_tokens_match(self, source, expected_t):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens() 
        self.assertEqual(len(tokens), len(expected_t))

        for actual, (e_type, e_lex, e_lit) in zip(tokens, expected_t):
            self.assertEqual(actual.type, e_type)
            self.assertEqual(actual.lexeme, e_lex)
            self.assertEqual(actual.literal, e_lit)
    
    def test_token_types(self):
        with open(DIR / "testtokens.txt") as f:
            source = f.read()
        expected = [
            (t.PAR_IZQ, "(", None),
            (t.PAR_DER, ")", None),
            (t.LLAVE_IZQ, "{", None),
            (t.LLAVE_DER, "}", None),
            (t.COMA, ",", None),
            (t.PUNTO, ".", None),
            (t.PUNTO_Y_COMA, ";", None),
            (t.NEGACION, "!", None),
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
            (t.CLASE, "clase", None),
            (t.SINO, "sino", None),
            (t.FALSO, "falso", None),
            (t.DEFINICION, "defi", None),
            (t.DESDE, "desde", None),
            (t.SI, "si", None),
            (t.NULO, "nulo", None),
            (t.O, "o", None),
            (t.IMPRIMIR, "imp", None),
            (t.RETORNAR, "retorna", None),
            (t.PADRE, "padre", None),
            (t.ESTE, "este", None),
            (t.CIERTO, "cierto", None),
            (t.SEA, "sea", None),
            (t.MIENTRAS, "mientras", None),
            (t.FIN, "", None)
        ]
        self.assert_tokens_match(source, expected)

    def test_comma_decimal(self):
        source = "3,14"
        expected = [
            (t.NUMERO, "3,14", 3.14),
            (t.FIN, "", None)
        ]
        self.assert_tokens_match(source, expected)

    def test_number(self):
        source = "3"
        expected = [
            (t.NUMERO, "3", 3.0),
            (t.FIN, "", None)
        ]
        self.assert_tokens_match(source, expected)

    def test_point_decimal(self):
        source = "3.14"
        expected = [
            (t.NUMERO, "3", 3.0),
            (t.PUNTO, ".", None),
            (t.NUMERO, "14", 14.0),
            (t.FIN, "", None)
        ]
        self.assert_tokens_match(source, expected)

    def test_accents(self):
        source = "árbol público médico íntimo ratón año"
        expected = [
            (t.IDENTIFICADOR, "árbol", None),
            (t.IDENTIFICADOR, "público", None),
            (t.IDENTIFICADOR, "médico", None),
            (t.IDENTIFICADOR, "íntimo", None),
            (t.IDENTIFICADOR, "ratón", None),
            (t.IDENTIFICADOR, "año", None),
            (t.FIN, "", None)
        ]
        self.assert_tokens_match(source, expected)

    def test_comments(self):
        source = '#this is a comment\n' \
        'sea a = "this is a string ####"'
        expected = [
            (t.SEA, "sea", None),
            (t.IDENTIFICADOR, "a", None),
            (t.ASIGNAR, "=", None),
            (t.CADENA, '"this is a string ####"', 'this is a string ####'),
            (t.FIN, "", None)
        ]
        self.assert_tokens_match(source, expected)

    @patch("scanner.ErrorHandler")
    def test_unexpected_character(self, mock_error):
        source = "@"
        scanner = Scanner(source)
        scanner.scan_tokens() 
        mock_error.error.assert_called_once_with(1, "Carácter no esperado.")

    @patch("scanner.ErrorHandler")
    def test_unterminated_string(self, mock_error):
        source = '"The neverending string....'
        scanner = Scanner(source)
        scanner.scan_tokens() 
        mock_error.error.assert_called_once_with(1, "Cadena no cerrada.")

    @patch("scanner.ErrorHandler")
    def test_recovery(self, mock_error):
        source = '$\n' \
                'sea a = 5\n' \
                '"The neverending string....'
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()
        mock_error.error.assert_any_call(1, "Carácter no esperado.")
        mock_error.error.assert_any_call(3, "Cadena no cerrada.")
        types = [token.type for token in tokens]
        self.assertIn(t.SEA, types)
        self.assertIn(t.IDENTIFICADOR, types)
        self.assertIn(t.ASIGNAR, types)
        self.assertIn(t.NUMERO, types)


if __name__ == "__main__":
    unittest.main()