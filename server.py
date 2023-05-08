import shared
import socket
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# serve at localhost port 1234
s.bind(shared.address)
s.listen(5)


def handle_conn(s, addr):
    try:
        while True:
            # receive a message
            msg = shared.receive(s)
            print(msg)
            match msg.split('\t'):
                case [''] | ['BYE', _]:
                    # if the message is empty, the client has disconnected I think
                    shared.send(s, "BYE\t")
                    s.close()
                    return
                case ['SAY', message]:
                    match msg:
                        case 'L2NsZWFudXA=': # if the message is equal to the /cleanup command, clear the messages older than 1 month
                            with open('messages.json', 'r+') as f:
                                msgs:list[dict]=eval(f.read())
                                msgs=[msg for msg in msgs if msg['time']>time.time()-2592000]
                                f.truncate(0)
                                f.seek(0)
                                f.write(str(msgs))
                        case _:
                            # otherwise, add the message to the messages file
                            with open('messages.json', 'r+') as f:
                                msgs:list[dict]=eval(f.read())
                                msgs.append({'time':time.time(),'message':message,'name':addr[0]})
                                f.truncate(0)
                                f.seek(0)
                                f.write(str(msgs))
                case ['GET MSG',from_time]:
                    with open('messages.json', 'r') as f:
                        msgs: list[dict] = eval(f.read())
                        msgs = [msg for msg in msgs if msg['time'] > float(from_time)]
                        shared.send(s, 'MSG ' + str(msgs))
                case ['GET IPT']:
                    with open('ipt.json', 'r') as f:
                        shared.send(s, 'IPT ' + f.read().replace('\n', ''))
                case ['SET IPT', name]:
                    with open('ipt.json', 'r+') as f:
                        ipt: dict = eval(f.read())
                        ipt[addr[0]] = name
                        f.truncate(0)
                        f.seek(0)
                        f.write(str(ipt))
                case ['GET PING']:
                    #  return the time in unix timestamp format
                    shared.send(s, 'PONG ' + str(time.time()))
                case _:
                    shared.send(s, 'ERR ' + msg)
                    print('error:')
                    print(msg)
    except ConnectionAbortedError:
        s.close()
        return
    except ConnectionResetError:
        s.close()
        return
    except ConnectionError:
        s.close()
        return
    except WindowsError:
        s.close()
        return


# accept a connection
while True:
    conn, addr = s.accept()
    # handle the connection in a new thread
    threading.Thread(target=handle_conn, args=(conn, addr)).start()
