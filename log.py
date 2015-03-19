from enum import Enum
import sys

class Log(Enum):

    INFO = 0
    WARN = 1
    ERR  = 2
    DEBUG= 3

    def log(msg, kind = INFO):
        if kind.value <= 0:
            sys.stderr.write(str(msg) + '\n')
        else:
            print(msg)
