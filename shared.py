"""A library for sending and receiving messages reliably over TCP sockets."""

import socket

address = ('localhost', 1234)

msgEnd = '\n'
codec = 'utf-8'


def cksum(msg: str):
    """Returns the checksum of a message."""
    try:
        return sum([ord(c) for c in msg]) % 256
    except ValueError:
        return sum([c for c in msg]) % 256


def send(sock: socket.socket, msg: str):
    sock.sendall(msg.encode(codec) + msgEnd.encode(codec) + cksum(msg).to_bytes(2, 'big'))


def receive(sock: socket.socket):
    msg = ''
    while msg[-1:] != msgEnd:
        msg += sock.recv(1).decode(codec)
    sm = int.from_bytes(sock.recv(2), 'big')
    if cksum(msg[:-1]) == sm:
        return msg[:-1]
    raise Exception("Message not received call our customer service in Nigeria")
