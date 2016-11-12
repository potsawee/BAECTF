import getpass
import sys
import telnetlib
import re

HOST = 'skillz.baectf.com'
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST, 31387)


tn.read_until("Enter password: ")
tn.write("avenue\n")
a = tn.read_until("Here are the numbers: ",2)

#get 4 numbers and find the sum

tn.write(sum+"\n")
key = tn.read_until(".",2)
print key
