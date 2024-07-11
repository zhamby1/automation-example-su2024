from twisted.internet import protocol,reactor
from twisted.internet.protocol import connectionDone
from twisted.python.failure import Failure

class EchoClient(protocol.Protocol):
    
    def connectionMade(self):
        self.transport.write(b"hello, world!")
    
    def dataReceived(self, data):
        #as soon as you receive a response display it
        print("Server said", data)
        self.transport.loseConnection()
    
    def connectionLost(self, reason):
        print("connection lost")

class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed - goodbye!")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost - goodbye!")
        reactor.stop()

def main():
    f = EchoFactory()
    reactor.connectTCP("localhost",8000,f)
    reactor.run()


if __name__ == "__main__":
    main()