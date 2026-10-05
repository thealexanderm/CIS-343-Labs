import sys

from error_handler import ErrorHandler
from scanner import Scanner


class Geco:
    def run(self, source):
        ErrorHandler.had_error = False
        for token in Scanner(source).scan_tokens():
            print(token)

    def run_file(self, path):
        with open(path, encoding="utf-8") as source_file:
            self.run(source_file.read())
        return 65 if ErrorHandler.had_error else 0

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
