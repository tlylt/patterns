# Base Class
class Logger:
    def __init__(self):
        self.content = []
    
    def log(self, message):
        self.content.append(message)
        return message

# Filtering
class LevelFilteredLogger(Logger):
    def __init__(self, level):
        self.level = level
        super().__init__()
    
    def log(self, message):
        if self.level in message:
            return super().log(message)

class LengthFilteredLogger(Logger):
    def __init__(self, length_limit):
        self.length_limit = length_limit
        super().__init__()
    
    def log(self, message):
        if len(message) < self.length_limit:
            return super().log(message)

# Log Destination
class STDOutLogger(Logger):
    def log(self, message):
        print(message)
        return super().log(message)

class FileLogger(Logger):
    def __init__(self, filename):
        self.filename = filename
        super().__init__()
    
    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\n')
        return super().log(message)

# Combination of Filtering and Log Destination
class LevelFilteredFileLogger(LevelFilteredLogger):
    def __init__(self, level, filename):
        self.filename = filename
        super().__init__(level)
    def log(self, message):
        msg = super().log(message)
        if msg:
            with open(self.filename, 'a') as f:
                f.write(msg + '\n')
        return msg


if __name__ == '__main__':
    logger = LevelFilteredFileLogger('ERROR', 'log.txt')
    logger.log('DEBUG: debug message')
    logger.log('INFO: info message')
    logger.log('ERROR: error message')
