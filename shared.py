import socket

msgEnd=''
msgAccept=''

def checksum(data):
    # Calculate the sum of all bytes in the data
    total = sum((ord(byte) if isinstance(byte,str) else byte) for byte in data)
    # Take the two's complement of the sum
    checksum = ~total & 0xFF
    return checksum

def sendMsg(s,msg):
    msg=msg+msgEnd
    msg=msg.encode('utf-8')
    msg=msg+bytes([checksum(msg)])
    s.sendall(msg)

def recvMsg(s):
    msg=b''
    while True:
        data=s.recv(1)
        if data==msgEnd.encode('utf-8'):
            break
        msg+=data
    return msg

def send(s, data, tries=0):
    while True:
        tries -= 1
        if tries == 0:
            return False
        sendMsg(s,data)
        msg=recvMsg(s)
        if msg==msgAccept.encode('utf-8'):
            break

def recieve(s, tries=0):
    while True:
        tries -= 1
        if tries == 0:
            return False
        msg=recvMsg(s)
        sendMsg(s,msgAccept)
        if checksum(msg)==0:
            break
    return msg[:-1].decode('utf-8')