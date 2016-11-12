import telnetlib

HOST = 'skillz.baectf.com'
tn = telnetlib.Telnet(HOST, 31387)

tn.read_until("Enter password: ")
tn.write("avenue")


print("we heard {}",format( msg))
#print tn.read_all()
