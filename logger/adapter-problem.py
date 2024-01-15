class FileHandler:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\n')

class FileLogger:
    def __init__(self, file_handler):
        self.file_handler = file_handler

    def log(self, message):
        self.file_handler.write(message)

class LevelFilteredLogger(FileLogger):
    def __init__(self, level, file_handler):
        self.level = level
        super().__init__(file_handler)
    
    def log(self, message):
        if self.level in message:
            super().log(message)
