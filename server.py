from libLocalH import LocalH

LocalH.InitSock
LocalH.LocalBind
LocalH.LocalLis

while True:
    # accept connections from outside
    (clientsocket, address) = LocalH.InitSock.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    ct = make_client_thread(clientsocket)
    ct.start()