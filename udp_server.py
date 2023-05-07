import socket

localIP='127.0.0.1'
if(not validate(localIP)):
    localIP='localhost'
localPort=5080
bufferSize=1024
Message='success'
Sendbytes=str.encode(Message)

while(True):
    UDPServerSocket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    if(UDPServerSocket.connect_ex((localIP,localPort))!=0):
        UDPServerSocket.close()
        break
    UDPServerSocket.close()
    UDPServerSocket:socket=socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP,localPort))
    print('listening')
    bytesAddressPair=UDPServerSocket.recvfrom(bufferSize)
    if(len(bytesAddressPair)==2):
        message=bytesAddressPair[0]
	address=bytesAddressPair[1]
	clientMsg=message.decode()                
        clientIP=address
        print(clientMsg)
        print(clientIP)
        UDPServerSocket.sendto(Sendbytes,address)
    UDPServerSocket.close()