class EmptyListError(Exception):
    def __init__(self, message):
        self.message = message

class FullListError(Exception):
    def __init__(self, message):
        self.message = message

class ExistingContactError(Exception):
    def __init__(self, message):
        self.message = message

class NonExistingContactError(Exception):
    def __init__(self, message):
        self.message = message

class HashKeyError(Exception):
    def __init__(self, message):
        self.message = message
