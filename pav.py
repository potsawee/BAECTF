import getpass
import sys
import telnetlib

HOST = 'skillz.baectf.com'
#password = getpass.getpass()

tn = telnetlib.Telnet(HOST, 31379)


tn.read_until("Enter password: ")
tn.write("ultrasonic\n")
a = tn.read_until("bit: ",2)
#print a

tn.write(a)
c = tn.read_until(".",2)

#print b +"\n"
#c = tn.read_all()
print c
