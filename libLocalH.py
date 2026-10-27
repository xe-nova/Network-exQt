import socket

class LocalH:
    InitSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def LocalCon():
        InitSock.connect(("localhost", 5000))
    def LocalSen():
        InitSock.send(("localhost", 5000))
    def LocalLis():
        InitSock.listen(5)
    def LocalBind(): 
        InitSock.bind(("localhost", 5000))
