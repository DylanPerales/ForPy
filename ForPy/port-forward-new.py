#!/usr/bin/python
from socket import *
bufsize = 1024 # Modify to suit your needs
targetHost = "127.0.0.1"
listenPort = 2500

def forward(data, port):
    print "Forwarding: '%s' from port %s" % (data, port)
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("0.0.0.0", port)) # Bind to the port data came in on
    sock.sendto(data, (targetHost, listenPort))

def listen(host, port):
    listenSocket = socket(AF_INET, SOCK_DGRAM)
    listenSocket.bind((host, port))
    while True:
        data, addr = listenSocket.recvfrom(bufsize)
        forward(data, addr[1]) # data and port

listen("0.0.0.0", listenPort)
