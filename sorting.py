import getpass
import sys
import telnetlib
import re

HOST = 'skillz.baectf.com'
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST, 31393)


tn.read_until("Enter password: ")
tn.write("ilikenumbers\n")
a = tn.read_until("Enter 1 or 2: ")
nums = a[102:-15]
print nums
