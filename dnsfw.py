#!/usr/bin/env python3

'''
This script will just show you what to write in our gateway / DNS to prevent
ip addresses to resolve domains, blocking DNS queries with iptables 
'''

import os
import sys

def usage():
    print("dnsfw.py <domain> [source]")
    print("This command will prevent 10.0.0.1 to resolve www.microsoft.com")
    print("dnsfw.py www.microsoft.com 10.0.0.1")

try:
    tokensList=sys.argv[1].split(".")
    commandList = ['iptables -A INPUT -p udp --dport 53 -m string --hex-string ']
except:
    usage()
    exit(1)
for i in range(len(tokensList)):
    tokenLenStr=str('{:02x}'.format(len(tokensList[i])))
    commandList.append("|"+tokenLenStr+"|"+tokensList[i])

try:
    commandList.append("| -s "+sys.argv[2]+" ")
    commandList.append("--algo bm -j DROP")
except:
    commandList.append("| --algo bm -j DROP")
print(''.join(commandList))

