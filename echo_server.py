#!/usr/bin/python

# echo server
from socket import *

host = ''
port = 6668

sock = socket(AF_INET, SOCK_STREAM)
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sock.bind((host,port))
sock.listen(1)
while True: # In Listening&Accept
	print "*** Listening..."
	conn,addr = sock.accept() #conn=sock, addr=(host,port)
	print "*** Connected"
	print "*** ",addr
	buf=""
	while True: #In Connect
		buf = conn.recv(1024)
		if buf:
			print buf
		else:
			print "*** Connection Finished"
			break
		conn.send(buf)
	conn.close()

