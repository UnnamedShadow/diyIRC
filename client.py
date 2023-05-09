import base64
import socket
import sys
import shared


# TODO: automatyczne GET MSG


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
          sep="\n")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(shared.address)
    print(f"connected with {shared.address[0]}:{shared.address[1]}")
    print("shortcuts:",
          "1: SAY",
          "2: GET MSG",
          "3: GET IPT",
          sep="\r\n")
    while True:
        command = input("enter a command: ")
        match command.split("\t"):
            case ["HELP" | "help" | "?"] | ["HELP" | "help" | "?", _]:
                print_help()
            case ["SAY", msg] | ["1", msg]:
                command = command.split("\t")
                command = "SAY" + "\t" + base64.b64encode(command[1].encode()).decode()
                shared.send(s, command)
            case ["GET MSG", from_time] | ["2", from_time]:
                command = command.split("\t")
                command = "GET MSG" + "\t" + str(base64.b64encode(command[1].encode()))
                shared.send(s, command)
                message = shared.receive(s)
                message = eval(message.split("\t")[1])
                message = "\r\n".join([base64.b64decode(i["message"]).decode() for i in message])
                print(message)
            case ["SET IPT", name]:
                shared.send(s, command)
            case ["GET IPT" | "GET PING"] | ["GET IPT" | "GET PING", _] | ["3"]:
                if command == "3":
                    command = "GET IPT"
                shared.send(s, command.split("\t")[0])
                print(shared.receive(s))
            case ["BYE", _] | ["BYE"]:
                print("connection ended")
                s.close()
                sys.exit()
            case _:
                print("invalid command")
                continue
