import socket

msg_end = b'\n'
msg_accept = b'\x06'

def checksum(data):
    """Calculate the two's complement checksum of the message data"""
    total = sum(data)
    checksum = (~total + 1) & 0xFF
    return checksum

def send_msg(s, msg):
    """Send a message over the socket connection"""
    msg = msg + msg_end
    checksum_value = checksum(msg)
    msg = msg + bytes([checksum_value])
    s.sendall(msg)

def recv_msg(s):
    """Receive a message over the socket connection"""
    msg = b''
    while True:
        data = s.recv(1)
        if data == msg_end:
            break
        msg += data
    recv_checksum = s.recv(1)
    expected_checksum = checksum(msg)
    if recv_checksum != bytes([expected_checksum]):
        send_msg(s, msg_accept)
        return None
    send_msg(s, msg_accept)
    return msg.decode('utf-8')

def send(s, data, tries=3):
    """Send data with retries"""
    while tries > 0:
        send_msg(s, data)
        msg = recv_msg(s)
        if msg is not None:
            return True
        tries -= 1
    return False

def receive(s, tries=3):
    """Receive data with retries"""
    while tries > 0:
        msg = recv_msg(s)
        if msg is not None:
            return msg
        tries -= 1
    return None
