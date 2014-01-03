# Author: Mario Scondo (www.Linux-Support.com)
# Date: 2010-01-08
# Script template by Stephen Chappell
#
# This script forwards a number of configured local ports
# to local or remote socket servers.
#
# Configuration:
# Add to the config file port-forward.config lines with
# contents as follows:
#   <local incoming port> <dest hostname> <dest port>
#
# Start the application at command line with 'python port-forward.py'
# and stop the application by keying in <ctrl-c>.
#
# Error messages are stored in file 'error.log'.
#

from __future__ import print_function
import socket
import sys
import thread
import time
 
def main(setup, error):
    # open file for error messages
    sys.stderr = file(error, 'a')
    # read settings for port forwarding
    for settings in parse(setup):
        thread.start_new_thread(server, settings)
    # wait for <ctrl-c>
    while True:
       time.sleep(60)
 
def parse(setup):
    settings = list()
    for line in file(setup):
        parts = line.split()
        settings.append((int(parts[0]), parts[1], int(parts[2])))
    return settings
 
def server(*settings):
    try:
        dock_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dock_socket.bind(('', settings[0]))
        dock_socket.listen(5)
        while True:
            client_socket = dock_socket.accept()[0]
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_socket.connect((settings[1], settings[2]))
            thread.start_new_thread(forward, (client_socket, server_socket))
            thread.start_new_thread(forward, (server_socket, client_socket))
    finally:
        thread.start_new_thread(server, settings)
 
def forward(source, destination):
    today = datetime.date.today()
    log = ('port-forward_' + today.strftime('%Y%b%d') + '.log')
    string = ' '
    while string:
        string = source.recv(1024)
        if string:
            destination.sendall(string)
            print('Forwarding: ' + source.getpeername() + ' Port: ' + source.getsockname(), file=log)
        else:
            source.shutdown(socket.SHUT_RD)
            destination.shutdown(socket.SHUT_WR)
	f.close()
if __name__ == '__main__':
    main('port-forward.config', 'error.log')