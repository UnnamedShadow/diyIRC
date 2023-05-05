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

all messages("\<message>") are sent in base64 encoded
time is sent in unix timestamp format

### Sending messages

client: `SAY <message>`

### receiving messages

client: `GET MSG <time>`
server: `MSG <json>`

### geting ip to name table

client: `GET IPT`  
server: `IPT <json>`

### send name to ip table

client: `SET IPT <name>`

### getting ping

client: `GET PING`
server: `PONG <time>`

### invalid request

server: `ERR <message>`
