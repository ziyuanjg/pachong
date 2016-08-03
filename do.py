#!/usr/bin/python3
# -*- coding: utf-8 -*-  放在文件头，表示文件编码
# Filename:do.py

import socket
from datetime import datetime

#address = ('localhost',6789)
#max_size =1000
#print("Start the client at {}".format(datetime.now()))
#client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#client.connect(address)
#client.send(b'Hey~~~')
#data = client.recv(max_size)
#print("AT",datetime.now(),"some reply" , data)
#client.close()

class aa():

    a=1
    b=2

va = aa()
print(aa.a)
print(va.a)


print(aa.a)
print(va.a)
va.a = 4
aa.a = 3
print(va.a)