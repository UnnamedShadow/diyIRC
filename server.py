import shared
import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serve at localhost port 1234
s.bind(('localhost', 1234))
s.listen(1)
# accept a connection
conn, addr = s.accept()
# send a message
shared.send(conn, 'Hello, world!')
# recieve a message
print(shared.recieve(conn))