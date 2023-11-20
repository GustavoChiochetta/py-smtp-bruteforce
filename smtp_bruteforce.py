#!/usr/bin/python
import socket,sys,re

print(len(sys.argv))

if (len(sys.argv) != 3):
    print('Usage: python smtp_bruteforce.py <ip address> wordlist.txt')
else:
    file = open(sys.argv[2])
    for line in file:
        print(line)
        tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp.connect((sys.argv[1],25))
        banner = tcp.recv(1024)
        tcp.send("VRFY "+line)
        user = tcp.recv(1024)
        if re.search("252",user):
            print("User found: "+user.strip("252 2.0.0"))
