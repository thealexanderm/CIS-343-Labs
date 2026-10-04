from error_handler import ErrorHandler
from gecko_token import Token
from token_type import TokenType as t


class Scanner:
    def __init__(self, source):
        self.source = source
        # TODO: initialize the scanner's state.
        self.start = 0
        self.current = 0
        self.line = 1
        self.tokens = []
        self.keywords = {
            "and": t.AND,
            "class": t.CLASS,
            "else": t.ELSE,
            "false": t.FALSE,
            "for": t.FOR,
            "fun": t.FUN,
            "if": t.IF,
            "nil": t.NIL,
            "or": t.OR,
            "print": t.PRINT,
            "return": t.RETURN,
            "super": t.SUPER,
            "this": t.THIS,
            "true": t.TRUE,
            "var": t.VAR,
            "while": t.WHILE,
        }

    def scan_tokens(self):
        """Return a list of Token objects, ending with one EOF token.

        Report lexical errors through ErrorHandler.error(line, message).
        Scanning begins at line 1. Ignore whitespace and // comments.
        """
        while not self.isAtEnd():
            self.start = self.current
            self.scan_token()

        self.tokens.append(Token(t.EOF, "", None, self.line))
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
            ErrorHandler.error(self.line, "Unterminated string.")
            return

    def isDigit(self, c):
        return c >= "0" and c <= "9"

    def peekNext(self):
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def number(self):
        while self.isDigit(self.peek()):
            self.advance()

        if self.peek() == "." and self.isDigit(self.peekNext()):
            self.advance()
            while self.isDigit(self.peek()):
                self.advance()

    def isAlpha(self, c):
        return (c >= "a" and c <= "z") or (c >= "A" and c <= "Z") or (c == "_")

    def isAlphaNumeric(self, c):
        return self.isDigit(c) or self.isAlpha(c)

    def identifier(self):
        while self.isAlphaNumeric(self.peek()):
            self.advance()

        text = self.source[self.start : self.current]
        type = self.keywords.get(text)
        if type is None:
            type = t.IDENTIFIER
        self.addToken(type)

    def scan_token(self):
        c = self.advance()
        match c:
            case "(":
                self.addToken(t.LEFT_PAREN)
            case ")":
                self.addToken(t.RIGHT_PAREN)
            case "}":
                self.addToken(t.RIGHT_BRACE)
            case "{":
                self.addToken(t.LEFT_BRACE)
            case ",":
                self.addToken(t.COMMA)
            case ".":
                self.addToken(t.DOT)
            case "-":
                self.addToken(t.MINUS)
            case "+":
                self.addToken(t.PLUS)
            case ";":
                self.addToken(t.SEMICOLON)
            case "*":
                self.addToken(t.STAR)
            case "!":
                self.addToken(t.BANG_EQUAL if self.match("=") else t.BANG)
            case "=":
                self.addToken(t.EQUAL_EQUAL if self.match("=") else t.EQUAL)
            case "<":
                self.addToken(t.LESS_EQUAL if self.match("=") else t.LESS)
            case ">":
                self.addToken(t.GREATER_EQUAL if self.match("=") else t.GREATER)

            case "/":
                if self.match("/"):
                    while self.peek() != "\n" and not self.isAtEnd():
                        self.advance()
                else:
                    self.addToken(t.SLASH)

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
                    ErrorHandler.error(self.line, "Unexpected character.")
