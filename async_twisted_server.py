from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    #this will receive a request and respon with the same data sent back to the client or user
    #aka a echo (client says hello server says hello back)
    def dataReceived(self,data):
        print(data)
        self.transport.write(data)

def main():
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(8000,factory)
    reactor.run()

if __name__ == "__main__":
    main()