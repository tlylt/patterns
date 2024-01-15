class STDOutLogger:
    def log(self, message):
        print(message)

class FileLogger:
    def __init__(self, filename):
        self.filename = filename
    
    def log(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\n')

class LevelFilteredLogger:
    def __init__(self, logger, level):
        self.logger = logger
        self.level = level

    def log(self, message):
        if self.level in message:
            self.logger.log(message)

class LengthFilteredLogger:
    def __init__(self, logger, length_limit):
        self.logger = logger
        self.length_limit = length_limit
    
    def log(self, message):
        if len(message) < self.length_limit:
            self.logger.log(message)


if __name__ == '__main__':
    file_logger = FileLogger('log.txt')
    file_logger.log('Hello World')

    std_out_logger = STDOutLogger()
    std_out_logger.log('Hello World')

    level_filtered_std_logger = LevelFilteredLogger(std_out_logger, 'INFO')
    level_filtered_std_logger.log('INFO: Hello World')
    level_filtered_std_logger.log('DEBUG: Hello World')

    length_filtered_file_logger = LengthFilteredLogger(file_logger, 10)
    length_filtered_file_logger.log('Hello World')
    length_filtered_file_logger.log('Hello')

    length_and_level_filtered_logger = LengthFilteredLogger(level_filtered_std_logger, 10)
    length_and_level_filtered_logger.log('INFO: Hello World Again')
    length_and_level_filtered_logger.log('DEBUG: Hello World')
    length_and_level_filtered_logger.log('INFO: HI')