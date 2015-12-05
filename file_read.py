#!/usr/bin/python

f=open("testfile")
buf=f.readline()
while buf:
	print buf,
	buf=f.readline()
