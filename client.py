import shared
import socket
from sys import exit

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(shared.address)
    print(f"connected with {shared.address[0]}:{shared.address[1]}")
    while True:
        command = input("enter a message: ")
        if command == "HELP" or command == "help" or command == "?":
            print("syntax: <command> tab <message>, for example SAY\tHello, world!")
            print("Here is the list of all available commands:")
            print("HELP / help / ?: prints this help",
                  "BYE: ends connection and stops execution of this program",
                  "SAY <message>: sends <message>",
                  "GET MSG <time>: receive messages sent after <time> (unix timestamp)",
                  "GET IPT: receive ip to name table",
                  "SET ITP <name>: binds <name> to your IP in IPT",
                  "GET PING: tests the connection",
                  sep="\n")
            continue
        shared.send(s, command)
        message = shared.receive(s)
        print(message)
        if "BYE" in message:
            print("connection ended")
            s.close()
            exit()
