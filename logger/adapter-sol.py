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
    def __init__(self, file_handler, level):
        self.level = level
        super().__init__(file_handler)
    
    def log(self, message):
        if self.level in message:
            super().log(message)

class STDOutHandler:
    def log(self, message):
        print(message)

class STDOutAdapter(FileHandler):
    def __init__(self):
        self.STDOutLogger = STDOutHandler()
        super().__init__(None)

    def write(self, message):
        self.STDOutLogger.log(message)

class LengthFilteredLogger(FileLogger):
    def __init__(self, file_handler, length_limit):
        self.length_limit = length_limit
        super().__init__(file_handler)
    
    def log(self, message):
        if len(message) < self.length_limit:
            super().log(message)


if __name__ == '__main__':
    file_handler = FileHandler('log.txt')
    file_logger = FileLogger(file_handler)
    file_logger.log('Hello World')

    std_out_handler = STDOutAdapter()
    std_out_logger = FileLogger(std_out_handler)
    std_out_logger.log('Hello World')

    level_filtered_file_logger = LevelFilteredLogger(std_out_handler, 'INFO')
    level_filtered_file_logger.log('INFO: Hello World')
    level_filtered_file_logger.log('DEBUG: Hello World')

    length_filtered_std_logger = LengthFilteredLogger(std_out_handler, 10)
    length_filtered_std_logger.log('Hello World')
    length_filtered_std_logger.log('Hello')