import shared
import socket
import threading
import time

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serve at localhost port 1234
s.bind(shared.address)
s.listen(5)

def handle_conn(s,addr):
    while True:
        # recieve a message
        msg = shared.recieve(s)
        match msg.split('\t'):
            case [''] | ['BYE']:
                # if the message is empty, the client has disconnected I think
                s.close()
                break
            case ['SAY', message]:
                pass #TODO: implement with some commands
            case ['GET MSG',from_time]:
                with open('messages.json', 'r') as f:
                    msgs:list[dict]=f.read()
                    msgs=[msg for msg in msgs if msg['time']>from_time]
                    shared.send(s, 'MSG '+str(msgs))
            case ['GET IPT']:
                with open('ipt.json', 'r') as f:
                    shared.send(s, 'IPT '+f.read().replace('\n',''))
            case ['SET IPT', name]:
                with open('ipt.json', 'w') as f:
                    ipt:dict=eval(f.read())
                    ipt[addr[0]]=name
                    f.write(str(ipt))
            case ['GET PING']:
                #  return the time in unix timestamp format
                shared.send(s, 'PONG '+str(time.time()))
            case _:
                    shared.send(s, 'ERR '+msg)
                    print('error:')
                    print(msg)

# accept a connection
while True:
    conn, addr = s.accept()
    # handle the connection in a new thread
    threading.Thread(target=handle_conn, args=(conn,addr)).start()
