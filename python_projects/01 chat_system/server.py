import socket
CHUNK = 65355 # recieve at most of these data at once
port = 3000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#create a socket object 
#socket.socket(family,type)
#AF_INET: family of ipv4 address
#SOCK_DIAGRAM: UDP, SOCK_STREAM: TCP

#some ip address that server will listen to when message comes
hostname = '127.0.0.1' 
#ip add of local machine and its same for everyone

s.bind((hostname,port)) #bind the socket with the host machine and on port 3000

print(f'server is live on {s.getsockname()}')

#Run this server infinitely till i stop manually

while True:
    data, clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii') #data by default travels in bytes
    print(f'Prabhat: {clientAdd} {message}')
    message_send = input ("Reply: ")

    data = message_send.encode("ascii") #send data to ip that sent me the data
    s.sendto(data, clientAdd)
