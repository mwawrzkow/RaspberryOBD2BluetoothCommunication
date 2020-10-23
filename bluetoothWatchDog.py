class Watchdog:
    def waitForData(self):
        return self.Socket.recv(1024)
    def sendData(self,data):
        return self.Socket.send(data)
    def __init__(self, clientSocket):
        self.Socket = clientSocket