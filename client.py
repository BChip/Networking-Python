#!/usr/bin/env python

import socket

IP = 'localhost'
PORT = 4000
BUFFER = 1024
MESSAGE = "Hello"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(MESSAGE)
res = s.recv(BUFFER)
s.close()

print "response: ", res