import bluetooth

class Server: 
    def __init__(self):
        self.hostMACAddress = ''
        self.port = 3  
        self.size = 1024
        self.backlog = 1 
        self.socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    def init(self): 
        self.socket.bind((self.hostMACAddress,self.port))
        self.socket.listen(self.backlog)

    def checkData(self):
        try: 
            client, clientInfo = self.socket.recv(self.size)
            data = client.recv(size)
            if data: 
                print(data)
                client.send(data) #echo
        except: 
            print("Closing socket")
            client.close() 
            self.socket.close() 


