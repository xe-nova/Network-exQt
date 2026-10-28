from libLocalH import LocalH

LocalH.LocalBind()
LocalH.LocalLis()

while True:
    RClientSocket, RAddress = LocalH.InitSock.accept()

    ct = make_client_thread(clientsocket)

    ct.start()
