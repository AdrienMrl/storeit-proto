#!/usr/bin/python

import json
from twisted.internet import protocol, reactor, endpoints

class Client(protocol.Protocol):

    def __init__(self):

        self.actions = {
            'HELO': Client.HELO,
            'LAST': Client.LAST,
            'ARBO': Client.ARBO
        }
        self.revision = 0

    def HELO(self, data):
        self.name = data

    def LAST(self, data):
        self.last_revision = data
        pass

    def ARBO(self, data):
        diffs = arbo_diff(json.loads(data))
        print(diffs)

    def connectionMade(self):
        #self.factory.clients.append(self)
        pass

    def dataReceived(self, data):
        data = data.split('\r\n')
        for d in data:
            words = d.split(' ', 1)
            try:
                self.actions[words[0]](self, words[1])
            except:
                pass

            #self.transport.write(data)

class ClientFactory(protocol.Factory):
    def buildProtocol(self, addr):
        # self.clients = []
        return Client()

if __name__ == '__main__':

    endpoints.serverFromString(reactor, "tcp:1234").listen(ClientFactory())
    reactor.run()
