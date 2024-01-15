class Logger:
    def __init__(self):
        self.log = []
    
    def log(self, message):
        self.log.append(message)

class LevelFilteredLogger(Logger):
    def __init__(self, level):
        self.level = level
        super().__init__()
    
    def log(self, message):
        if self.level in message:
            super().log(message)

class LengthFilteredLogger(Logger):
    def __init__(self, length_limit):
        self.length_limit = length_limit
        super().__init__()
    
    def log(self, message):
        if len(message) < self.length_limit:
            super().log(message)

class STDOutLogger(Logger):
    def log(self, message):
        print(message)
        super().log(message)

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename
        super().__init__()
    
    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\n')
        super().log(message)

class LevelFilteredFileLogger(LevelFilteredLogger):
    def __init__(self, level, filename):
        self.filename = filename
        super().__init__(level)
    
    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\n')
        super().log(message)