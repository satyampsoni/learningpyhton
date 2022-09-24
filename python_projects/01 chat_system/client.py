import socket 
port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
CHUNK = 65535

#instead of explicitly bindig the socket this time let os will to do it
#empheral ports: Ports are assigned by os
#os will bind this for us

hostname = '127.0.0.1'
while True:
    s.connect((hostname,port))
    message = input("Type message: ")
    data = message.encode("ascii")
    s.send(data)
    #data recieved
    data = s.recv(CHUNK)
    text = data.decode("ascii")
    print(f'Satyam: {text}')
