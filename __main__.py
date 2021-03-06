# import BluetoothSocket as bs
import bluetooth
import ConnectionAutomatize
import os
import OBD2Port
import bluetoothWatchDog

if os.system("hciconfig hci0 piscan") == -1:
    print("Run it as root!")
    exit
def serverConnection():
    server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    # port = bluetooth._get_available_ports( bluetooth.RFCOMM )
    server_sock.bind(("",0))
    server_sock.listen(1)
    print ("listening on port: 0")

    uuid = "5dc85d5b-4bdd-40ca-ab9c-c700c088c6c4"
    bluetooth.advertise_service( server_sock, "FooBar Service", uuid )
    obd2 = OBD2Port.OBDInterpreter()
    data = "" 
    while data != b"Exit":
        client_sock,address = server_sock.accept()
        print ("Accepted connection from :")
        print(address)
        data = client_sock.recv(1024)
        if data == b"EnX88hsumpCFAqBxr#ckpL!7X7G+eDCEyLGq!Bc?X-^s5$BJm*PGfD!tnBtj7f8B@5!XL=Bu#?8p$sAeWUMK=2+5HAXBe9=VhTwE":
            print("Connection accepted")
            client_sock.send(b"Accept")
            while data != b"Exit":
                wd = bluetoothWatchDog.Watchdog(client_sock)
                data = wd.waitForData()
                response =ConnectionAutomatize.RequestAction(data,obd2)
                wd.sendData(response)



        #client_sock.send(data)
        data = client_sock.recv(1024)

    client_sock.close()
    server_sock.close()
while True:
    try:
        serverConnection()
    except:
        print("Error Occured!")
        pass
