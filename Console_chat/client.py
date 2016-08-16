#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
import socket

config = configparser.ConfigParser()
config.read("chat-config.cfg")
host = config.get("DATA","host")
port = int(config.get("DATA","port"))
byte_per_package = int(config.get("DATA","byte_per_package"))

sock = socket.socket()
sock.connect((host, port))

print("Enter your message or press 'q' to exit")

while True:
      client_data = input()
      if client_data == "q":
          break
      sock.send(client_data.encode())
      
      server_data = sock.recv(byte_per_package)
      print (server_data.decode())

sock.send(client_data.encode())      
print("Connection closed")      
sock.close()
