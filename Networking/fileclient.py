## create a file client that will send the name of the file it want and display the contents of file.

import socket              #importing a socket module


s=socket.socket()           #create a object
s.connect(('localhost',8080))   # connect to server

fileName=input("enter a file name:")
s.send(fileName.encode())
content=s.recv(1024)
print(content.decode())
s.close()
