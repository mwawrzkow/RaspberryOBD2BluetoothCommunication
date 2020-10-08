import bluetooth

server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
# port = bluetooth._get_available_ports( bluetooth.RFCOMM )
server_sock.bind(("",0))
server_sock.listen(1)
print ("listening on port: 0")

uuid = "5dc85d5b-4bdd-40ca-ab9c-c700c088c6c4"
bluetooth.advertise_service( server_sock, "FooBar Service", uuid )

client_sock,address = server_sock.accept()
print ("Accepted connection from :")
print(address)

data = client_sock.recv(1024)
print ("received [ ")
print(data)
print("]")

client_sock.close()
server_sock.close()
