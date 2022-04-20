from base64 import encode
import getpass
import telnetlib
from telnet1 import HOST

## HOST = "192.168.211.153"
user = input("Enter the username: ")
password = getpass.getpass("Enter the password: ")

for i in range (3,5):
    HOST = "192.168.211.15" + str(i)
    print("Telnet Ip address: " + HOST)
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

        tn.write(b"vlan " + str(j).encode('ascii') + b"\n")
        tn.write(b"name vlan_" + str(j).encode('ascii') + b"\n")
        tn.write(b"exit\n")

        if j == 4 :
            tn.write(b"interface vlan 4\n")
            tn.write(b"ip address 2.2.4.2 255.255.255.0\n")
            tn.write(b"no shutdown\n")
            tn.write(b"exit\n")
        if j == 5:
            tn.write(b"interface vlan 5\n")
            tn.write(b"ip address 2.2.5.1 255.255.255.0\n")
            tn.write(b"no shutdown\n")
            tn.write(b"exit\n")


tn.write(b"exit\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))
tn.close
