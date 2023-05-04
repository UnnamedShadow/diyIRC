import shared
import socket
import threading

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serve at localhost port 1234
s.bind(shared.address)
s.listen(1)

def handle_conn(s,addr):
    shared.send(s, 'hi there '+str(addr))
    # recieve a message
    print(shared.recieve(s))

# accept a connection
while True:
    conn, addr = s.accept()
    # handle the connection in a new thread
    threading.Thread(target=handle_conn, args=(conn,addr)).start()
