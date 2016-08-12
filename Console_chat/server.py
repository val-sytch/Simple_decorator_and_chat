#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('Connected:', addr)
while True:
    client_data = conn.recv(1024)
    client_data = client_data.decode()
    if client_data == "q":
        break
    print(client_data)
    server_data = input()
    conn.send(server_data.encode())
    
print("Connection closed")
conn.close()
