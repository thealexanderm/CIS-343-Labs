from error_handler import ErrorHandler
from geco_token import Token
from token_type import Tipo as t


class Scanner:
    def __init__(self, source):
        self.source = source
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []
        self.keywords = {
            "y": t.Y,
            "clase": t.CLASE,
            "sino": t.SINO,
            "falso": t.FALSO,
            "desde": t.DESDE,
            "defi": t.DEFINICION,
            "si": t.SI,
            "nulo": t.NULO,
            "o": t.O,
            "imp": t.IMPRIMIR,
            "retorna": t.RETORNAR,
            "padre": t.PADRE,
            "este": t.ESTE,
            "cierto": t.CIERTO,
            "sea": t.SEA,
            "mientras": t.MIENTRAS,
        }

    def scan_tokens(self):
        """Return a list of Token objects, ending with one FIN token.

        Report lexical errors through ErrorHandler.error(line, message).
        Scanning begins at line 1. Ignore whitespace and # comments.
        """
        while not self.isAtEnd():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(t.FIN, "", None, self.line))
        return self.tokens

    def match(self, expected):
        if self.isAtEnd():
            return False
        if self.source[self.current] != expected:
            return False

        self.current += 1
        return True

    def isAtEnd(self):
        return self.current >= len(self.source)

    def advance(self):
        c = self.source[self.current]
        self.current += 1
        return c

    def addToken(self, type, literal=None):
        text = self.source[self.start : self.current]
        self.tokens.append(Token(type, text, literal, self.line))

    def peek(self):
        if self.isAtEnd():
            return "\0"
        return self.source[self.current]

    def string(self):
        while self.peek() != '"' and not self.isAtEnd():
            if self.peek() == "\n":
                self.line += 1
            self.advance()

        if self.isAtEnd():
            ErrorHandler.error(self.line, "Cadena no cerrada.")
            return

        self.advance()
        value = self.source[self.start + 1 : self.current - 1]
        self.addToken(t.CADENA, value)

    def isDigit(self, c):
        return c >= "0" and c <= "9"

    def peekNext(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def number(self):
        while self.isDigit(self.peek()):
            self.advance()

        if self.peek() == "," and self.isDigit(self.peekNext()):
            self.advance()
            while self.isDigit(self.peek()):
                self.advance()

        self.addToken(t.NUMERO, float(self.source[self.start : self.current].replace(",", ".")))

    def isAlpha(self, c):
        return c.isalpha() or (c == "_")

    def isAlphaNumeric(self, c):
        return self.isDigit(c) or self.isAlpha(c)

    def identifier(self):
        while self.isAlphaNumeric(self.peek()):
            self.advance()
        text = self.source[self.start : self.current]
        type = self.keywords.get(text)
        if type is None:
            type = t.IDENTIFICADOR
        self.addToken(type)

    def scan_token(self):
        c = self.advance()
        match c:
            case "(":
                self.addToken(t.PAR_IZQ)
            case ")":
                self.addToken(t.PAR_DER)
            case "}":
                self.addToken(t.LLAVE_DER)
            case "{":
                self.addToken(t.LLAVE_IZQ)
            case ",":
                self.addToken(t.COMA)
            case ".":
                self.addToken(t.PUNTO)
            case "-":
                self.addToken(t.MENOS_ASIGNAR if self.match("=") else t.MENOS)
            case "+":
                self.addToken(t.MAS_ASIGNAR if self.match("=") else t.MAS)
            case ";":
                self.addToken(t.PUNTO_Y_COMA)
            case "*":
                self.addToken(t.ESTRELLA_ASIGNAR if self.match("=") else t.ESTRELLA)
            case "/":
                self.addToken(t.DIV_ASIGNAR if self.match("=") else t.BARRA)
            case "!":
                self.addToken(t.NO_IGUAL if self.match("=") else t.NEGACION)
            case "=":
                self.addToken(t.IGUAL_IGUAL if self.match("=") else t.ASIGNAR)
            case "<":
                self.addToken(t.MENOR_IGUAL if self.match("=") else t.MENOR)
            case ">":
                self.addToken(t.MAYOR_IGUAL if self.match("=") else t.MAYOR)
            case "%":
                self.addToken(t.MODULO_ASIGNAR if self.match("=") else t.MODULO)

            case "#":
                while self.peek() != "\n" and not self.isAtEnd():
                    self.advance()

            case " " | "\r" | "\t":
                pass
            case "\n":
                self.line += 1
            case '"':
                self.string()

            case _:
                if self.isDigit(c):
                    self.number()
                elif self.isAlpha(c):
                    self.identifier()
                else:
                    ErrorHandler.error(self.line, "Carácter no esperado.")
