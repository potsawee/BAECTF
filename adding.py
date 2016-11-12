import telnetlib

HOST = 'skillz.baectf.com'
tn = telnetlib.Telnet(HOST, 31387)

tn.read_until("Enter password: ")
tn.write("avenue")

message = tn.read_until("ppp", 10)
#print("we heard {}",format( msg))
print("we heard222 {}".format( message))
#print tn.read_all()
