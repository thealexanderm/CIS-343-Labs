import sys
from scanner import Scanner
from error_handler import ErrorHandler


class Gecko:
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
        print("Usage: python3 src/gecko/gecko.py [script", file=sys.stderr)
        print("Or: python3 src/gecko/gecko.py", file=sys.stderr)
        return 64
    gecko = Gecko()
    return gecko.run_file(sys.argv[1] if len(sys.argv) == 2 else gecko.run_prompt())


if __name__ == "__main__":
    sys.exit(main())
