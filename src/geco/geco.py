import sys
from error_handler import ErrorHandler
from scanner import Scanner
from parser import Parser
from interpreter import Interpreter


class Geco:
    def run(self, source):
        ErrorHandler.had_error = False
        tokens = Scanner(source).scan_tokens()
        parser = Parser(tokens)
        statements = parser.parse()
        if ErrorHandler.had_error:
            return

        print(Interpreter().interpret(statements))

    def run_file(self, path):
        with open(path, encoding="utf-8") as source_file:
            self.run(source_file.read())
        if ErrorHandler.had_error:
            return 65
        return 70 if ErrorHandler.hadRuntimeError else 0

    def run_prompt(self):
        while True:
            try:
                source = input("> ")
            except (EOFError, KeyboardInterrupt):
                print()
                return 0
            self.run(source)


def main():
    if len(sys.argv) > 2:
        print("Uso: python3 src/geco/geco.py [archivo]", file=sys.stderr)
        print("O: python3 src/geco/geco.py", file=sys.stderr)
        return 64
    geco = Geco()
    return geco.run_file(sys.argv[1]) if len(sys.argv) == 2 else geco.run_prompt()


if __name__ == "__main__":
    sys.exit(main())
