import shared
import socket
import threading
import time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serve at localhost port 1234
s.bind(shared.address)
s.listen(1)

def handle_conn(s,addr):
    shared.send(s, 'hi there '+str(addr))
    # recieve a message
    print(shared.recieve(s))
    while True:
        # recieve a message
        msg = shared.recieve(s)
        if msg=='':
                # if the message is empty, the client has disconnected I think
                s.close()
                break
        elif msg[:3]=='SAY':
            pass
        elif msg[:7] == 'GET MSG':
            pass
        elif msg=='GET IPT':
            with open('ipt.txt', 'r') as f:
                shared.send(s, 'IPT '+f.read())
        elif msg[:7]=='SET IPT':
            pass
        elif msg[:8]=='GET PING':
            #  return the time in unix timestamp format
            shared.send(s, 'PONG '+str(time.time()))
        else:
                shared.send(s, 'ERR '+msg)
                print('error:')
                print(msg)

# accept a connection
while True:
    conn, addr = s.accept()
    # handle the connection in a new thread
    threading.Thread(target=handle_conn, args=(conn,addr)).start()
