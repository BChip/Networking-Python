#!/usr/bin/env python

import socket

IP = 'localhost'
PORT = 4000
BUFFER = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((IP, PORT))
s.listen(True)

conn, addr = s.accept()
while True:
    data = conn.recv(BUFFER)
    if not data: break
    conn.send(data.upper() + " LENGTH: " + str(len(data)))
conn.close()