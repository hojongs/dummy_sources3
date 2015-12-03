from socket import *

host='127.0.0.1'
port=6667
size=1024

sock=socket(AF_INET, SOCK_STREAM)

sock.connect((host,port))
sock.send('hello')
print sock.recv(size)