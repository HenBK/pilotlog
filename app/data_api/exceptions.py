

class BadFileError(Exception):
    default_exception_message = 'Invalid file format.'

    def __init__(self, message=default_exception_message):
        self.message = message or self.default_exception_message
        super().__init__(self.message)
