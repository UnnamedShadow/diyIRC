import shared
import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(shared.address)
shared.send(s, input('enter a message: '))
print(shared.recieve(s))
s.close()
