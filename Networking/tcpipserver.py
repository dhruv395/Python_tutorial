import socket
host='localhost'
port=4000

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #default is tcp ipv4 #SOCK_STREAM=tcp;socket.AF_INET=ipv4
s.bind((host,port))
print("server listening on port:",port)
s.listen(1)                                         # no of clients server will connect to
c,addr = s.accept()                                 #establishes a connection with the server when a client request comes in
print("connection from: ",str(addr))                #convert address to string format

c.send(b"hello, how are you?")                      ## send mesg to client in binary format (b)
c.send("bye".encode())                              ## or send mesg to client in binary format (encoding)
c.close()
