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

client: `SAY\t<message>`

### Receiving messages

client: `GET MSG\t<time>`  
server: `MSG\t<json>`

### Geting ip to name table

client: `GET IPT`  
server: `IPT\t<json>`

### Send name to ip table

client: `SET IPT\t<name>`

### Getting ping

client: `GET PING`  
server: `PONG\t<time>`

### Invalid request

server: `ERR\t<message>`
