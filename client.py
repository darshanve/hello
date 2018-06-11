import socket

s = socket.socket()

server = '192.168.43.87'
port = 12346

s.connect((server,port))
print("Got connected to server")

while True :
    msg  = s.recv(1024).decode()
    if msg == 'bye':
        print("Connection Terminated by server")
        s.close()
    print("\t\t\tServer->",msg)
    m = input("Client->")
    s.send(m.encode())
