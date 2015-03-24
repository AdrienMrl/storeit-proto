from log import Log
from log import Log
from arbo import Arbo
from protocol import Proto
import os
import json

class Client:

    def get_last_update():
        return open('.storeit/last_update').read()

    def __init__(self):

        try:
            os.makedirs('.storeit')
            Arbo.write_file('.storeit/last_update', '0')

        except IOError as e:
            Log.log('cannot make base directory', Log.WARN) # check for errors here

        self.arbo = Arbo.get()
#        print(arbo)
#        exit(0)

        self.com = Proto()
        self.com.send('HELO Sevauk')
        self.com.send('LAST ' + Client.get_last_update())
        self.com.send('ARBO ' + json.dumps(self.arbo))

        self.actions = {
            'SEND': self.SEND,
            'RECV': self.RECV
        }

    def run(self):

        while True:
            data = self.com.recv()
            if not data: break
            for cmd in data:
                words = cmd.split(' ', 1)
                if words[0] in actions:
                    self.actions[words[0]](words[1].split(' '))
                else:
                    Log.log('unknown command ' + words[0], Log.ERR)

    def SEND(self, args):
        print('will receive')
        pass

    def RECV(self, args):
        print('will send')
        pass
