from socket import *


host=''
port=6667
size=1024

ssock=socket(AF_INET,SOCK_STREAM)
ssock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

ssock.bind((host,port))
ssock.listen(1)
csock,addr=ssock.accept()
print addr

buf=csock.recv(size)
print buf
csock.send(buf)
csock.close()
ssock.close()