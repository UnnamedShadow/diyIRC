"""A library for sending and receiving messages reliably over TCP sockets."""

import socket

address=('localhost',1234)

msgEnd='\n'
codec='utf-8'

def cksum(msg):
    """Returns the checksum of a message."""
    try:
        return sum([ord(c) for c in msg]) % 256
    except ValueError:
        return sum([c for c in msg]) % 256

def send(sock, msg):
    msg = msg + msgEnd + chr(cksum(msg))
    sock.sendall(msg.encode(codec))

def recieve(sock):
    msg = ''
    while msg[-1:] != msgEnd:
        msg += sock.recv(1).decode(codec)
    sm=ord(sock.recv(2).decode(codec))
    if cksum(msg[:-1]) == sm:
        return msg[:-1]
    raise Exception("Message not received call our customer service in Nigeria")