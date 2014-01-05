#!/usr/bin/python
from __future__ import print_function
from socket import *
import time
import os

# Settings
bufsize = 1024 # Modify to suit your needs
targetHost = "127.0.0.1" # Modify to remote Address OR LOOP WILL OCCUR!!!
listenAddr = "0.0.0.0"
listenPort = 2500
pkts = 0
if not os.path.exists('log'):
    os.makedirs('log')

# Log Info
log = ('log/port-forward_' + time.strftime('%Y%m%d') + '.log')

# Forward Method
def forward(data, addr):
    with open(log, 'a') as f:
        f.write("%s - Pkt%s: Recieved: %s[%s] Forwarded to: %s\n" % (time.strftime('%Y%m%d %H:%m:%S'), pkts, addr[0], data, targetHost))
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(("0.0.0.0", addr[1])) # Bind to the port data came in on
    sock.sendto(data, (targetHost, listenPort))

# Listen Method
def listen(host, port):
    listenSocket = socket(AF_INET, SOCK_DGRAM)
    listenSocket.bind((host, port))
    while True:
        data, addr = listenSocket.recvfrom(bufsize)
        global pkts
        pkts += 1
        forward(data, addr) # data and port

listen(listenAddr, listenPort)
