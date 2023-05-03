"""A library for sending and receiving messages reliably over TCP sockets."""

import socket

msgEnd=''
msgAccept=''
tries=5

def cksum(msg):
    """Returns the checksum of a message."""
    try:
        return sum([ord(c) for c in msg]) % 256
    except ValueError:
        return sum([c for c in msg]) % 256

def send(sock, msg):
    """Sends a message over a socket. Until confirmation is received. Or the message is sent 3 times."""
    msg = msg + msgEnd + chr(cksum(msg))
    for i in range(tries):
        sock.sendall(msg)
        if sock.recv(1) == msgAccept:
            return
    raise Exception("Message not sent")

def recv(sock):
    """Receives a message over a socket."""
    msg = ''
    for i in range(tries):
        msg = ''
        while msg[-1:] != msgEnd:
            msg += sock.recv(1)
        msg = msg[:-1]
        if cksum(msg) == ord(sock.recv(1)):
            sock.sendall(msgAccept)
            return msg
    raise Exception("Message not received")
