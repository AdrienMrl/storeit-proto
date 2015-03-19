import socket

class Proto:
    def __init__(self, port = 1234, host = socket.gethostname()):
        self.s = socket.socket()

        self.s.connect((host, port))

    def send(self, msg):
        self.s.send(bytearray(msg + "\r\n", 'utf-8'))

    def recv(self):
        data = str()
        buf = str()

        while True:
            buf += s.recv(2048)
            if buf == '':
                break
            data += buf
        data = data.decode('utf-8')
        for command in data.split('\r\n')
            yield command
        return ''


    def __del__(self):
        self.s.close()
