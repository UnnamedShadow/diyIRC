import base64
import socket
import sys
import shared


# TODO: cli, automatyczne GET MSG, opcje zamiast inputu


def print_help():
    print("syntax: <command> tab <message>, for example SAY\thello there")
    print("Here is the list of all available commands:")
    print("HELP / help / ?: prints this help",
          "BYE: ends connection and stops execution of this program",
          "SAY <message>: sends <message>",
          "GET MSG <time>: receive messages sent after <time> (unix timestamp)",
          "GET IPT: receive ip to name table",
          "SET IPT <name>: binds <name> to your IP in IPT",
          "GET PING: tests the connection",
          "AUTO GET MSG: automatically display messages sent to the server",
          sep="\n")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(shared.address)
    print(f"connected with {shared.address[0]}:{shared.address[1]}")
    while True:
        command = input("enter a message: ")
        match command.split("\t"):
            case ["HELP" | "help" | "?"] | ["HELP" | "help" | "?", _]:
                print_help()
                continue
            case ["GET MSG", from_time]:
                command = command.split("\t")
                command = command[0] + "\t" + str(base64.b64encode(command[1].encode()))
                shared.send(s, command)
                message = shared.receive(s)
                message = eval(message.split("\t")[1])
                message = "\n".join([base64.b64decode(i["message"]).decode() for i in message])
                print(message)
                continue
            case ["BYE", _] | ["BYE"]:
                print("connection ended")
                s.close()
                sys.exit()
        shared.send(s, command)
# GET MSG   1