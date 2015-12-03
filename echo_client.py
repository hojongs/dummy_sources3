#!/usr/bin/python

# echo client
from socket import *

host = 'localhost'
port = 6668

sock = socket(AF_INET, SOCK_STREAM)
sock.connect((host,port))
while True:
	print "input : ",
	buf=raw_input()
	sock.send(buf)
	if not buf:
		break
	buf = sock.recv(1024)
	print "receive : "+buf
sock.close()
