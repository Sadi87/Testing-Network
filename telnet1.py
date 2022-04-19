import getpass
import telnetlib

HOST = "192.168.211.153"
user = "admin"
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"en\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
for j in range(2,10):

        tn.write(b"vlan " +str(j) + "\n")

        tn.write(b"name " "vlan_" +str(j) + "\n")

        tn.write(b"end\n")

        tn.write(b"exit\n")

tn.write(b"end\n")


print(tn.read_all().decode('ascii'))
tn.close
