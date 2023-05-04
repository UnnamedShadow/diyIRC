import shared
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(shared.address)
print(shared.recieve(s))
shared.send(s, 'Hello, world!')