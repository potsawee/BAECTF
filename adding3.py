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


arr = re.findall(r'(\d+)',a)

tn.write(str(int(arr[2]) + int(arr[3]) + int(arr[4]) + int(arr[5])) + "\n")

b = tn.read_until("Here are the numbers: ",2)
c = b[100:]
print c
