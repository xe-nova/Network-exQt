import socket

class LocalH:
    InitSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def LocalCon():
        LocalH.InitSock.connect(("localhost", 5000))
    def LocalSen():
        LocalH.InitSock.send(("localhost", 5000))
    def LocalLis():
        LocalH.InitSock.listen(5) 
    def LocalBind(): 
        LocalH.InitSock.bind(("localhost", 5000))
