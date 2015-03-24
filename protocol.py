import socket

#TODO: handle larger files

class Proto:
    def __init__(self, port = 1234, host = socket.gethostname()):
        self.s = socket.socket()

        self.s.connect((host, port))

    def send(self, msg):
        print('sending ' + msg)
        self.s.send(bytearray(msg + "\r\n", 'utf-8'))

    def recv(self):
        buf = str()

        buf = self.s.recv(2048).decode('utf-8')
        if not buf:
            return
        return buf.split('\r\n')[:-1]


    def __del__(self):
        self.s.close()
