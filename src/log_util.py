import logging

# https://docs.python.org/3/library/logging.html#logrecord-attributes
LOG_FORMAT = '[%(asctime)s] [%(name)s] %(levelname)s: %(message)s'

COLOR_RESET = '\x1b[0m'

COLOR_RED = '\x1b[38;5;1m'
COLOR_GREEN = '\x1b[38;5;2m'
COLOR_YELLOW = '\x1b[38;5;3m'
COLOR_BLUE = '\x1b[38;5;4m'
COLOR_PURPLE = '\x1b[38;5;5m'
COLOR_GRAY = '\x1b[38;5;8m'

COLOR_LIGHT_BLUE = '\x1b[38;5;6m'
COLOR_LIGHT_RED = '\x1b[38;5;9m'
COLOR_LIGHT_GREEN = '\x1b[38;5;10m'
COLOR_LIGHT_YELLOW = '\x1b[38;5;11m'

COLOR_CYAN = '\x1b[38;5;14m'
COLOR_HIGHLIGHTS = '\x1b[38;5;15m'
COLOR_BRIGHT_RED = '\x1b[38;5;160m'

level_color = {
    "INFO": COLOR_RESET,
    "DEBUG": COLOR_GRAY,
    "WARNING": COLOR_YELLOW,
    "ERROR": COLOR_RED,
    "CRITICAL": COLOR_BRIGHT_RED
}

class Formatter(logging.Formatter):

    def format(self, record):

        color = level_color[record.levelname]
        level = record.levelname
        message = record.msg
        
        record.levelname = f'{color}{level}{COLOR_RESET}' 
        record.msg = f'{color}{message}{COLOR_RESET}'

        return super().format(record)

class Log:

    def __init__(self, name, is_debug=None) -> None:

        self.logger = logging.getLogger(name)
        
        if is_debug:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)

        handle = logging.StreamHandler()
        format = Formatter(LOG_FORMAT)
        handle.setFormatter(format)

        self.logger.addHandler(handle)

    def get_logger(self):
        return self.logger

def print_color_codes():
    for i in range(1, 255):
        code = f'\x1b[38;5;{i}m'
        print(f'{code }color of {code.encode()}')
