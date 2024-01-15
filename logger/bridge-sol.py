import abc

class Handler:
    @abc.abstractmethod
    def write(self, message):
        pass

class STDOutHandler:
    def write(self, message):
        print(message)

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\n')

class Logger:
    def __init__(self, handler):
        self.handler = handler
    
    def log(self, message):
        self.handler.write(message)

class LevelFilteredLogger(Logger):
    def __init__(self, handler, level):
        self.level = level
        super().__init__(handler)
    
    def log(self, message):
        if self.level in message:
            super().log(message)

class LengthFilteredLogger(Logger):
    def __init__(self, handler, length_limit):
        self.length_limit = length_limit
        super().__init__(handler)
    
    def log(self, message):
        if len(message) < self.length_limit:
            super().log(message)


if __name__ == '__main__':
    file_handler = FileHandler('log.txt')
    file_logger = Logger(file_handler)
    file_logger.log('Hello World')

    std_out_handler = STDOutHandler()
    std_out_logger = Logger(std_out_handler)
    std_out_logger.log('Hello World')

    level_filtered_std_logger = LevelFilteredLogger(std_out_handler, 'INFO')
    level_filtered_std_logger.log('INFO: Hello World')
    level_filtered_std_logger.log('DEBUG: Hello World')

    length_filtered_file_logger = LengthFilteredLogger(file_handler, 10)
    length_filtered_file_logger.log('Hello World')
    length_filtered_file_logger.log('Hello')
    