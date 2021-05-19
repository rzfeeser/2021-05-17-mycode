#!/usr/bin/env python3

# python3 -m pip install netifaces
import netifaces

# this will display a list of all interfaces avail
print(netifaces.interfaces())

# i becomes a single interface within a list of interfaces we have avail
for i in netifaces.interfaces():
    print(f'\n********Details of Interface - {i} ************') # print out i
    print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
    print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address

