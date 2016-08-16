#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import socket

config = configparser.ConfigParser()
config.read("chat-config.cfg")
port = int(config.get("DATA","port"))
max_connection_inline = int(config.get("DATA","max_connection_inline"))
byte_per_package = int(config.get("DATA","byte_per_package"))


sock = socket.socket()
sock.bind(('',port))
sock.listen(max_connection_inline)
conn, addr = sock.accept()

print ('Connected:', addr)
while True:
    client_data = conn.recv(byte_per_package)
    client_data = client_data.decode()
    if client_data == "q":
        break
    print(client_data)
    server_data = input()
    conn.send(server_data.encode())
    
print("Connection closed")
conn.close()

