from token_type import Tipo


class ErrorHandler:
    had_error = False
    hadRuntimeError = False

    # @staticmethod
    # def error(line, message):
    #     ErrorHandler.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print(f"[línea {line}] Error{where}: {message}")
        ErrorHandler.had_error = True

    @staticmethod
    def error(token, message):
        try:
            if token.type == Tipo.FIN:
                ErrorHandler.report(token.line, " al final", message)
            else:
                ErrorHandler.report(token.line, " en '" + token.lexeme + "'", message)
        except:
            ErrorHandler.report(token, "", message)

    @staticmethod
    def runtimeError(error):
        print(f"{str(error)} [línea {error.token.line}]")
        ErrorHandler.hadRuntimeError = True
