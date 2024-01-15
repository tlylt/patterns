class Logger:
    def __init__(self, filters, handlers):
        self.filters = filters
        self.handlers = handlers
    
    def log(self, message):
        if all(f.should_keep(message) for f in self.filters):
            for h in self.handlers:
                h.write(message)

class LevelFilter:
    def __init__(self, level):
        self.level = level
    def should_keep(self, message):
        return self.level in message

class LengthFilter:
    def __init__(self, length_limit):
        self.length_limit = length_limit
    def should_keep(self, message):
        return len(message) < self.length_limit

class FileHandler:
    def __init__(self, filename):
        self.filename = filename
    def write(self, message):
        with open(self.filename, 'a') as f:
            f.write(message + '\n')

class STDOutHandler:
    def write(self, message):
        print(message)

if __name__ == '__main__':
    file_handler = FileHandler('log.txt')
    length_file_logger = Logger([LengthFilter(10)], [file_handler])
    length_file_logger.log('Hello World')

    std_out_handler = STDOutHandler()
    level_std_out_logger = Logger([LevelFilter('INFO')], [std_out_handler])
    level_std_out_logger.log('INFO: Hello World')

    length_and_level_logger = Logger([LengthFilter(10), LevelFilter('INFO')], [file_handler, std_out_handler])
    length_and_level_logger.log('INFO: Hello World')