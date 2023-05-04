# diyIRC

an IRC like app

with a server and a client

## How to use

### Server

enter the downloaded directory and run:

```bash
python3 server.py
```

### Client

enter the downloaded directory and run:

```bash
python3 client.py
```

## Protocol

### Sending messages

client: `SAY <message>`

### receiving messages

server: `MSG <ip> <timestamp> <message>`

### sending commands

client: `CMD <command>`

### geting ip to name table

client: `GET IPT`  
server: `IPT <json>`
