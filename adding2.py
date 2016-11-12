import getpass
import sys
import telnetlib

HOST = 'skillz.baectf.com'
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST, 31387)


tn.read_until("Enter password: ")
tn.write("avenue\n")
a = tn.read_until("Here are the numbers: ",2)



#print "HIIIIIi"
print a
#print "PUNPUN"
