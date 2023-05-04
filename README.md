# diyIRC

an IRC like app

with a server and a client

## How to use

### Server

```bash
python3 server.py
```

### Client

```bash
python3 client.py
```

## Protocol

### Sending messages

client: `SAY <message>`

### receiving messages

server: `MSG <ip> <message>`

### sending commands

client: `CMD <command>`

### geting ip to name table

client: `GET IP`
server: `IP <json>`
