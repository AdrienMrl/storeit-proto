#!/usr/bin/python

import json
from swarm import Swarm
from twisted.internet import protocol, reactor, endpoints

class Client(protocol.Protocol):

    def __init__(self):

        self.actions = {
            'HELO': Client.HELO,
            'LAST': Client.LAST,
            'ARBO': Client.ARBO
        }
        self.revision = 0
        self.swarm = Swarm()
        self.ip_addr = None

    def send(self, data):
        print('sending: ' + data)
        self.transport.write(str(data + '\r\n').encode('utf-8'))

    def HELO(self, data):
        self.name = data

    def LAST(self, data):
        self.last_revision = data
        pass

    #def arbo_diff(self, new_arbo):
    #    print(new_arbo)
    #    print(self.arbo
    #    self.send('THIS IS A COMMAND')
    #    return 'here is the diff'


    def ARBO(self, data):
        #diffs = self.arbo_diff(json.loads(data).sort())
        #print(diffs)
        self.arbo = json.loads(data)
        self.swarm.add(self)

    def connectionMade(self):
        self.ip_addr = self.transport.getHost().host

    def dataReceived(self, data):
        data = data.split('\r\n')
        for d in data:
            words = d.split(' ', 1)
            if words[0] in self.actions:
                self.actions[words[0]](self, words[1])

class ClientFactory(protocol.Factory):
    def buildProtocol(self, addr):
        # self.clients = []
        return Client()

if __name__ == '__main__':

    endpoints.serverFromString(reactor, "tcp:1234").listen(ClientFactory())
    reactor.run()
