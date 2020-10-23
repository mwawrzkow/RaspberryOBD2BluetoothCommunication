class Watchdog:
    def waitForData(self):
        data = self.Socket.recv(1024)
        print(data)
        return data
    def sendData(self,data):
        print(data)
        return self.Socket.send(data.encode("UTF-8"))
    def __init__(self, clientSocket):
        self.Socket = clientSocket