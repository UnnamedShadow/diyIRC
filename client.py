import shared
import socket
from sys import exit

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(shared.address)
    print(f"connected with {shared.address[0]}:{shared.address[1]}")
    print(shared.receive(s))
    while True:
        command = input("enter a message: ")
        if command == "HELP" or command == "help" or command == "?":
            print("This is help for diyIRC client.")
            print("Here is the list of all available commands:")
            print("QUIT: ends connection and stops execution of this program",
                  "SAY <message>: sends <message> to the server",
                  "GET MSG <time>: receive messages sent in <time>",
                  "GET IPT: receive ip to name table",
                  "SET ITP <name>: binds <name> to your IP in IPT",
                  "GET PING: tests the connection",
                  sep="\n")
            continue
        shared.send(s, command)
        message = shared.receive(s)
        print(message)
        if message == "BYE":
            print("connection ended")
            s.close()
            exit()
