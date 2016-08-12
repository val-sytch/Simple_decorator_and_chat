#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

print("Enter your message or press 'q' to exit")

while True:
      client_data = input()
      if client_data == "q":
          break
      sock.send(client_data.encode())
      
      server_data = sock.recv(1024)
      print (server_data.decode())

sock.send(client_data.encode())      
print("Connection closed")      
sock.close()
