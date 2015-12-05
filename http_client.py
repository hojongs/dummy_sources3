#!/usr/bin/python

import urllib2

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0'),('Cookie','_cfduid=d2c7917ef252cd95305384390ae9e90671448667038; PHPSESSID=jdu3isqocr3otljs193cir86h6')]
response = opener.open('http://los.sandbox.cash/gate.php')

print response.read(10000)

