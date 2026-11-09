class RtimeError(RuntimeError):
    def __init__(self, token, message) -> None:
        super().__init__(message)
        self.token = token
